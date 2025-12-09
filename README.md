<h1>Metal Surface Defect Analyzer (XAI)</h1>

<p>
    An Automated Optical Inspection (AOI) system that couples high-performance metal surface defect detection with Explainable AI (XAI) to ensure trust and transparency.
</p>

<p>
    This project uses <b>YOLOv8</b> for defect detection and <b>Eigen-CAM</b> to generate gradient-free visual heatmaps, allowing users to understand where and why the model identified a defect.
</p>

<hr>

<h2>Key Features</h2>
<ul>
    <li>High-Accuracy Detection: Powered by YOLOv8m, achieving 77.5% mAP@0.5 across 6 defect classes (Crazing, Inclusion, Patches, Pitted Surface, Rolled-in Scale, Scratches).</li>
    <li>Explainable AI (XAI): Integrated Eigen-CAM (Principal Component Analysis of feature maps) to visualize model attention without heavy computational overhead.</li>
    <li>Dynamic Layer Probing: Interactive UI allows users to switch between network layers (e.g., Layer 2 vs. Layer 9) to verify feature extraction.</li>
    <li>Efficient Deployment: Flask-based web interface with decoupled inference logic and AJAX-based heatmap generation.</li>
</ul>

<hr>

<h2>Tech Stack</h2>
<ul>
    <li>Model: YOLOv8 Medium (PyTorch)</li>
    <li>XAI Library: pytorch-grad-cam (EigenCAM)</li>
    <li>Backend: Flask (Python)</li>
    <li>Frontend: HTML5, JavaScript (Fetch API)</li>
    <li>Processing: OpenCV, NumPy</li>
</ul>

<hr>

<h2>Usage</h2>

<ol>
    <li>
        Run the Flask Application:
        <br>
        <code>python app.py</code>
    </li>
    <br>
    <li>
        Access the Interface:
        <br>
        Open your browser and navigate to <code>http://127.0.0.1:5000</code>.
    </li>
    <br>
    <li>
        Analyze:
        <br>
        Upload a metal surface image, view bounding boxes, and select layers (e.g., <code>model.9</code>) to generate heatmaps.
    </li>
</ol>

<hr>

<h2>Performance Highlights</h2>
<ul>
    <li><b>Overall Accuracy:</b> 77.5% mAP@0.5</li>
    <li><b>Best Class (Scratches):</b> 97.4%</li>
</ul>
</p>
