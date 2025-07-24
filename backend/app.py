"""
Flask API for Digit Recognition

This app receives base64-encoded handwritten digit images (from a canvas),
preprocesses them, and returns predictions using a trained neural network.

Dependencies:
 - Flask
 - Flask-CORS
 -  Pillow (PIL)
 - NumPy
 - A trained model accessible via `predictNum()` in src/Model/predict.py

To run:
    python app.py
App will be available at http://localhost:5001
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from io import BytesIO
import base64
import numpy as np
import sys
import os
from PIL import Image, ImageOps, ImageChops

# Add model path so we can import from src/Model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(current_dir, '..', 'src', 'Model')
sys.path.insert(0, model_dir)
from predict import predictNum

app = Flask(__name__)
CORS(app)

# Keep track of previous predictions in memory
submission_history = []


def preprocess_base64_image(b64_png: str) -> np.ndarray:
    """
    Converts a base64-encoded canvas image to a (784, 1) vector suitable for model input.

    Returns:
        np.ndarray: Preprocessed image vector (shape: 784x1)
    """
    # Step 1: Decode base64 image (strip header)
    img_bytes = base64.b64decode(b64_png.split(",", 1)[1])
    img = Image.open(BytesIO(img_bytes)).convert("L")  # Convert to grayscale

    # Step 2: Crop to bounding box
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)

    # Step 3: Pad image to make it square
    w, h = img.size
    side = max(w, h)
    pad_left   = (side - w) // 2
    pad_top    = (side - h) // 2
    pad_right  = side - w - pad_left
    pad_bottom = side - h - pad_top
    img = ImageOps.expand(img, (pad_left, pad_top, pad_right, pad_bottom), fill=0)

    # Step 4: Center image using center-of-mass
    arr = np.asarray(img, dtype=np.float32)
    ys, xs = np.nonzero(arr)
    if xs.size:
        com_x, com_y = xs.mean(), ys.mean()
        shift_x = int(round(side / 2 - com_x))
        shift_y = int(round(side / 2 - com_y))
        img = ImageChops.offset(img, shift_x, shift_y)

    # Step 5: Resize to 28x28 (using nearest neighbor to preserve strokes)
    img = img.resize((28, 28), resample=Image.NEAREST)

    # Step 6: Normalize pixel values to [0, 1] and flatten
    arr = np.asarray(img, dtype=np.float32) / 255.0
    return arr.reshape(784, 1)


@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict endpoint — accepts a base64 image and returns a digit prediction.
    """
    data = request.get_json()

    if 'image' not in data:
        return jsonify({'error': 'No image provided'}), 400

    try:
        img_vec = preprocess_base64_image(data['image'])
        prediction = predictNum(img_vec)

        # Save this prediction to history
        submission_history.append({
            'image': data['image'],
            'prediction': int(prediction)
        })

        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/history', methods=['GET'])
def history():
    """
    Returns all previous predictions made in this session.
    """
    return jsonify({'history': submission_history})


@app.route('/ping', methods=['GET'])
def ping():
    """
    Simple health check endpoint.
    """
    return jsonify({'message': 'pong'})


if __name__ == '__main__':
    # Run the app locally on port 5001
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)
