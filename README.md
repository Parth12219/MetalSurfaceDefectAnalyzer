<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metal Surface Defect Analyzer (XAI)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Custom style for code blocks to look like terminals */
        .code-block {
            background-color: #1e1e1e;
            color: #d4d4d4;
            padding: 1rem;
            border-radius: 0.5rem;
            font-family: 'Courier New', Courier, monospace;
            overflow-x: auto;
            margin-top: 0.5rem;
            margin-bottom: 1rem;
        }
        .cmd-prefix::before {
            content: "$ ";
            color: #10b981; /* Green color for the prompt */
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans leading-relaxed">

    <header class="bg-blue-900 text-white py-16">
        <div class="max-w-4xl mx-auto px-6 text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-4">🔬 Metal Surface Defect Analyzer (XAI)</h1>
            <p class="text-xl text-blue-200">
                A real-time Automated Optical Inspection (AOI) system coupling high-performance object detection with Explainable AI.
            </p>
            <div class="mt-8">
                <a href="#installation" class="bg-white text-blue-900 font-bold py-2 px-6 rounded-full hover:bg-blue-100 transition duration-300">Get Started</a>
                <a href="https://github.com/yourusername/metal-defect-xai" class="ml-4 border border-white text-white font-bold py-2 px-6 rounded-full hover:bg-white hover:text-blue-900 transition duration-300">View on GitHub</a>
            </div>
        </div>
    </header>

    <main class="max-w-4xl mx-auto px-6 py-12">

        <section class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 border-b pb-2">Overview</h2>
            <p class="mb-4">
                This project uses <strong>YOLOv8</strong> for defect detection and <strong>Eigen-CAM</strong> to generate gradient-free visual heatmaps. It addresses the "Black Box" problem in industrial inspection by allowing operators to understand <em>where</em> and <em>why</em> the model identified a defect.
            </p>
        </section>

        <section class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 border-b pb-2">🚀 Key Features</h2>
            <div class="grid md:grid-cols-2 gap-6">
                <div class="bg-white p-6 rounded-lg shadow-md border-l-4 border-blue-600">
                    <h3 class="font-bold text-lg mb-2">High-Accuracy Detection</h3>
                    <p class="text-gray-600">Powered by <strong>YOLOv8m</strong>, achieving <strong>77.5% mAP@0.5</strong> across 6 distinct defect classes.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md border-l-4 border-purple-600">
                    <h3 class="font-bold text-lg mb-2">Explainable AI (XAI)</h3>
                    <p class="text-gray-600">Integrated <strong>Eigen-CAM</strong> to visualize model attention without heavy computational overhead.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md border-l-4 border-green-600">
                    <h3 class="font-bold text-lg mb-2">Dynamic Layer Probing</h3>
                    <p class="text-gray-600">Interactive UI allows users to switch between network layers (e.g., Layer 2 vs. Layer 9) to verify feature extraction.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-md border-l-4 border-orange-600">
                    <h3 class="font-bold text-lg mb-2">Efficient Deployment</h3>
                    <p class="text-gray-600"><strong>Flask-based</strong> web interface with decoupled inference logic and AJAX-based heatmap generation.</p>
                </div>
            </div>
        </section>

        <section class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 border-b pb-2">📸 Screenshots</h2>
            <div class="bg-gray-200 rounded-lg h-64 flex items-center justify-center text-gray-500 mb-4">
                [Place UI Screenshot Here]
            </div>
            <p class="text-sm text-center text-gray-500 italic">Figure 1: The analysis interface showing bounding boxes and XAI heatmaps side-by-side.</p>
        </section>

        <section class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 border-b pb-2">🛠️ Tech Stack</h2>
            <ul class="list-disc list-inside space-y-2 text-gray-700 bg-white p-6 rounded-lg shadow-sm">
                <li><strong>Model:</strong> YOLOv8 Medium (PyTorch)</li>
                <li><strong>XAI Library:</strong> <code>pytorch-grad-cam</code> (EigenCAM)</li>
                <li><strong>Backend:</strong> Flask (Python)</li>
                <li><strong>Frontend:</strong> HTML5, Tailwind CSS, JavaScript (Fetch API)</li>
                <li><strong>Processing:</strong> OpenCV, NumPy</li>
            </ul>
        </section>

        <section id="installation" class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 border-b pb-2">⚙️ Installation</h2>
            
            <div class="mb-6">
                <h3 class="font-bold text-xl mb-2">1. Clone the repository</h3>
                <div class="code-block">
                    <div class="cmd-prefix">git clone https://github.com/yourusername/metal-defect-xai.git</div>
                    <div class="cmd-prefix">cd metal-defect-xai</div>
                </div>
            </div>

            <div class="mb-6">
                <h3 class="font-bold text-xl mb-2">2. Install dependencies</h3>
                <div class="code-block">
                    <div class="cmd-prefix">pip install -r requirements.txt</div>
                </div>
            </div>

            <div class="mb-6">
                <h3 class="font-bold text-xl mb-2">3. Setup Weights</h3>
                <p class="mb-2">Place your trained model weights file (<code>best.pt</code>) in the correct directory, or update <code>WEIGHTS_PATH</code> in <code>model_utils.py</code>.</p>
                <div class="code-block">
                    MSDD_YOLOv8m_640/weights/best.pt
                </div>
            </div>
        </section>

        <section class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 border-b pb-2">🏃‍♂️ Usage</h2>
            <ol class="list-decimal list-inside space-y-4 text-gray-700">
                <li class="pl-2">
                    <strong>Run the Flask Application:</strong>
                    <div class="code-block mt-2">
                        <div class="cmd-prefix">python app.py</div>
                    </div>
                </li>
                <li class="pl-2">
                    <strong>Access the Interface:</strong><br>
                    Open your browser and navigate to <a href="http://127.0.0.1:5000" class="text-blue-600 hover:underline">http://127.0.0.1:5000</a>.
                </li>
                <li class="pl-2">
                    <strong>Analyze:</strong><br>
                    Upload a metal surface image, view bounding box predictions, and use the dropdown menu to select layers (e.g., <code>model.9</code>) for XAI visualization.
                </li>
            </ol>
        </section>

        <section class="mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 border-b pb-2">📊 Performance</h2>
            <div class="bg-white overflow-hidden shadow-sm rounded-lg">
                <table class="min-w-full">
                    <tbody class="divide-y divide-gray-200">
                        <tr>
                            <td class="px-6 py-4 font-medium text-gray-900">Overall mAP@0.5</td>
                            <td class="px-6 py-4 text-gray-700">77.5%</td>
                        </tr>
                        <tr>
                            <td class="px-6 py-4 font-medium text-gray-900">Best Class</td>
                            <td class="px-6 py-4 text-gray-700">Scratches (97.4%)</td>
                        </tr>
                        <tr>
                            <td class="px-6 py-4 font-medium text-gray-900">Inference Speed</td>
                            <td class="px-6 py-4 text-gray-700">Real-time (Sub-second)</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

    </main>

</body>
</html>
