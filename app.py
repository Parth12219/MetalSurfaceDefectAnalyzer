import os
import secrets
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from model_utils import predict_and_draw_boxes, generate_new_heatmap

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['SECRET_KEY'] = secrets.token_hex(16) 

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(input_path)

            predicted_img_url, results_data, initial_heatmap_url = predict_and_draw_boxes(
                input_path, app.config['OUTPUT_FOLDER']
            )
            
            session['current_image_path'] = input_path

            heatmap_url_to_render = None
            if initial_heatmap_url:
                heatmap_url_to_render = initial_heatmap_url.replace('\\', '/')

            predicted_img_url = predicted_img_url.replace('\\', '/')

            return render_template(
                'index.html', 
                predicted_img=predicted_img_url,
                heatmap_img=heatmap_url_to_render,
                results=results_data
            )
            
    return render_template('index.html')
@app.route('/get_heatmap', methods=['POST'])
def get_heatmap():
    layer_name = request.form.get('layer_name')
    
    image_path = session.get('current_image_path')
    
    if not image_path:
        return {"error": "No image found in session. Please re-upload."}, 400
        
    heatmap_url = generate_new_heatmap(
        image_path, 
        layer_name, 
        app.config['OUTPUT_FOLDER']
    )
    
    if heatmap_url is None:
        return {"error": "Heatmap generation failed on the server."}, 500

    heatmap_url = heatmap_url.replace('\\', '/')

    return {"heatmap_url": heatmap_url}


if __name__ == '__main__':
    app.run(debug=True)
