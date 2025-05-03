# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from io import BytesIO
import base64
import numpy as np
import sys, os

from PIL import Image, ImageOps, ImageChops  ### NEW ###
# ---------------------------------------------------------------------

# Path to current model (adjust if you move files)
sys.path.insert(1, '../src/Model')
from predict import predictNum

app = Flask(__name__)
CORS(app)

# Store history of predictions
submission_history = []

# ---------------------------------------------------------------------
#                      Pre‑processing helper
# ---------------------------------------------------------------------
def preprocess_base64_image(b64_png: str) -> np.ndarray:
    """
    Convert the base‑64 PNG from the canvas to a (784, 1) float32 vector
    ready for the network.
    """
    # 1  strip header & decode
    img_bytes = base64.b64decode(b64_png.split(",", 1)[1])
    img = Image.open(BytesIO(img_bytes)).convert("L")      # grayscale


    # 3  crop to the digit’s bounding box
    bbox = img.getbbox()          # (left, upper, right, lower) or None
    if bbox:                      # guard against empty drawings
        img = img.crop(bbox)

    # 4  pad to square
    w, h = img.size
    side = max(w, h)
    pad_left   = (side - w) // 2
    pad_top    = (side - h) // 2
    pad_right  = side - w - pad_left
    pad_bottom = side - h - pad_top
    img = ImageOps.expand(img, (pad_left, pad_top, pad_right, pad_bottom), fill=0)

    # 5  (OPTIONAL) centre by centre‑of‑mass à la LeCun
    arr = np.asarray(img, dtype=np.float32)
    ys, xs = np.nonzero(arr)
    if xs.size:
        com_x, com_y = xs.mean(), ys.mean()
        shift_x = int(round(side / 2 - com_x))
        shift_y = int(round(side / 2 - com_y))
        img = ImageChops.offset(img, shift_x, shift_y)

    # 6  resize to 28 × 28 (nearest keeps strokes crisp)
    img = img.resize((28, 28), resample=Image.NEAREST)

    # 7  scale to 0‑1 and flatten
    arr = np.asarray(img, dtype=np.float32) / 255.0
    return arr.reshape(784, 1)
# ---------------------------------------------------------------------

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if 'image' not in data:
        return jsonify({'error': 'No image provided'}), 400

    try:
        # --- preprocess -------------------------------------------------
        img_vec = preprocess_base64_image(data['image'])
        # ----------------------------------------------------------------

        # make prediction
        prediction = predictNum(img_vec)

        # save to history
        submission_history.append({
            'image': data['image'],
            'prediction': int(prediction)
        })

        return jsonify({'prediction': int(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/history', methods=['GET'])
def history():
    return jsonify({'history': submission_history})


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

# from flask import Flask, request, jsonify
# import base64
# from io import BytesIO
# import numpy as np
# import os
# import sys
# from PIL import Image
# from flask_cors import CORS

# #Path to current model
# sys.path.insert(1, '../src/Model')
# from predict import predictNum




# app = Flask(__name__)
# CORS(app)

# #store hstory of predictions
# submission_history = []

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     # print("Received data:", data.keys()) 

#     if 'image' not in data:
#         return jsonify({'error': 'No image provided'}), 400
    
#     try:
#         #decode base64 image
#         base64_str = data['image'].split(',')[1]
#         img_bytes = base64.b64decode(base64_str)
#         img = Image.open(BytesIO(img_bytes)).convert('L') #converts image to grayscale

#         #resize to 28x28
#         img = img.resize((28, 28), resample=Image.LANCZOS)
#         img_array = np.asarray(img) / 255.0
#         img_array = (img_array).astype(np.float32)
#         img_array = img_array.reshape(784, 1)

#         #make prediction
#         prediction = predictNum(img_array)
#         # print("predicting")

#         submission_history.append({
#             'image': data['image'],
#             'prediction': prediction
#         })

#         return jsonify({'prediction': int(prediction)})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
    
# @app.route('/history', methods=['GET'])
# def history():
#     return jsonify({'history': submission_history})

# @app.route('/ping', methods=['GET'])
# def ping():
#     return jsonify({'message': 'pong'})



# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001, debug=True)

