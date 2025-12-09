import os
import cv2
import pandas as pd
from ultralytics import YOLO
import numpy as np
import torch
from torch import nn

from pytorch_grad_cam import EigenCAM as LibraryEigenCAM
from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget 

WEIGHTS_PATH = r'MSDD_YOLOv8m_640\weights\best.pt' 
CLASS_NAMES = [
    'crazing', 'inclusion', 'patches', 'pitted_surface', 
    'rolled-in_scale', 'scratches'
]
MODEL_IMG_SIZE = 640 

class YOLOv8CAMWrapper(nn.Module):
    def __init__(self, model):
        super(YOLOv8CAMWrapper, self).__init__()
        self.model = model

    def forward(self, x):
        outputs = self.model(x)
        return outputs[0]

try:
    MODEL = YOLO(WEIGHTS_PATH)
    MODEL.to('cpu') 
    print("YOLO Model loaded successfully.")
    
except Exception as e:
    print(f"Error loading model: {e}")
    MODEL = None

def preprocess_image(img_bgr, img_size=640):
    img_resized = cv2.resize(img_bgr, (img_size, img_size))
    img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
    input_tensor = (torch.from_numpy(img_rgb).permute(2, 0, 1).float() / 255.0).unsqueeze(0)
    return input_tensor

def overlay_heatmap(original_img, heatmap, alpha=0.5, colormap=cv2.COLORMAP_JET):
    heatmap_resized = cv2.resize(heatmap, (original_img.shape[1], original_img.shape[0]))
    heatmap_uint8 = (heatmap_resized * 255).astype(np.uint8) 
    heatmap_color = cv2.applyColorMap(heatmap_uint8, colormap)
    overlay = cv2.addWeighted(original_img, 1 - alpha, heatmap_color, alpha, 0)
    return overlay

def find_target_layer_module(model, layer_name):
    for name, module in model.model.named_modules():
        if name == layer_name:
            return module
    raise ValueError(f"Target layer {layer_name} not found in model.")

def predict_and_draw_boxes(image_path, output_dir):
    if MODEL is None:
        print("\nERROR: MODEL NOT LOADED")
        return None, [], None

    output_subfolder = os.path.basename(output_dir)
    base_filename = os.path.splitext(os.path.basename(image_path))[0]
    predicted_filename = f"{base_filename}_predicted.jpg"
    predicted_full_path = os.path.join(output_dir, predicted_filename)

    original_img_np = cv2.imread(image_path)
    results = MODEL(image_path, conf=0.25, iou=0.5, verbose=False)
    result = results[0] 
    
    img_with_bboxes = result.plot(labels=True, conf=True)
    cv2.imwrite(predicted_full_path, img_with_bboxes)
    
    results_list = []
    if result.boxes and len(result.boxes) > 0:
        for box in result.boxes:
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            name = CLASS_NAMES[cls]
            
            explanation_text = RATIONALE_MAP.get(name, "No specific rationale found.")
            
            results_list.append({
                'name': name,
                'confidence': f"{conf:.2f}",
                'explanation': explanation_text 
            })
    else:
        results_list.append({
            'name': 'No Defect',
            'confidence': 'N/A',
            'explanation': 'No defects were detected by the model.'
        })

    initial_heatmap_url = generate_new_heatmap(image_path, "9", output_dir)
    
    predicted_url = os.path.join(output_subfolder, predicted_filename)
    
    return predicted_url, results_list, initial_heatmap_url
def generate_new_heatmap(image_path, layer_name, output_dir):
    if MODEL is None:
        return None
        
    try:
        target_layer_module = find_target_layer_module(MODEL.model, layer_name)
        target_layers = [target_layer_module]
        
        wrapped_model = YOLOv8CAMWrapper(MODEL.model)
        
        cam = LibraryEigenCAM(model=wrapped_model, target_layers=target_layers)

        original_img_np = cv2.imread(image_path)
        input_tensor = preprocess_image(original_img_np, img_size=MODEL_IMG_SIZE)
        
        grayscale_cam = cam(input_tensor=input_tensor, targets=None)
        heatmap_np = grayscale_cam[0, :]
            
        if heatmap_np is not None:
            heatmap_overlay = overlay_heatmap(original_img_np, heatmap_np)
            
            base_filename = os.path.splitext(os.path.basename(image_path))[0]
            layer_str = layer_name.replace('.', '_')
            heatmap_filename = f"{base_filename}_heatmap_{layer_str}.jpg"
            heatmap_full_path = os.path.join(output_dir, heatmap_filename)
            
            cv2.imwrite(heatmap_full_path, heatmap_overlay)
            print(f"Library EigenCAM heatmap for {layer_name} saved successfully.")
            return os.path.join(os.path.basename(output_dir), heatmap_filename)
        else:
            raise Exception("CAM generator returned None.")

    except Exception as e:
        print(f"XAI Error on layer {layer_name}: {e}.")
        return None

RATIONALE_MAP = {
    'crazing': "Model focused on fine, web-like textural patterns.",
    'inclusion': "Model focused on a distinct, sharp-edged object that breaks the surface pattern.",
    'patches': "Model focused on a discolored or rough-textured area with an irregular shape.",
    'pitted_surface': "Model focused on small, dark, circular depressions or 'dot-like' features.",
    'rolled-in_scale': "Model focused on a large, embedded patch with a different texture.",
    'scratches': "Model focused on strong, thin, linear features (lines)."
}
