"""
Digit Recognition Script

This script loads a trained neural network from a pickle file and uses it to 
predict the digit shown in an input image. It also provides a utility function 
for predicting digits using a preprocessed input vector.

Dependencies:
 - neural_network.py (contains the `Network` class)
 - saved_model.pkl (trained model file)
 -  Pillow, NumPy, and pickle
"""

from neural_network import Network
import pickle
from PIL import Image, ImageOps
import numpy as np

def predict():
    """
    Loads an image, preprocesses it, and predicts the digit using a trained neural network.
    """
    # Load trained model from pickle file
    with open("saved_model.pkl", "rb") as f:
        model_data = pickle.load(f)

    # Reconstruct the neural network
    net = Network(model_data["sizes"])
    net.biases = model_data["biases"]
    net.weights = model_data["weights"]

    # Load and preprocess image
    img = Image.open("sample_images/6.jpg")       # Load input image
    img_adjusted = img.convert("L").resize((28, 28))   # Convert to grayscale and resize
    img_adjusted = ImageOps.invert(img_adjusted)      # Invert colors (white digit on black background)

    img_adjusted.save("processed_img.png")             

    # Normalize pixel values and flatten into 784x1 vector
    img_array = np.array(img_adjusted).astype(np.float32) / 255.0
    img_flat = img_array.reshape(784, 1)

    # Predict and print result
    prediction = net.predict(img_flat)
    print("Predicted digit:", prediction)

def predictNum(img_flat):
    """
    Predicts the digit from a preprocessed 784x1 input vector.

    Parameters:
    img_flat (np.ndarray): A flattened and normalized (784, 1) image vector

    Returns:
    int: Predicted digit
    """
    with open("../saved_model.pkl", "rb") as f:
        model_data = pickle.load(f)

    net = Network(model_data["sizes"])
    net.biases = model_data["biases"]
    net.weights = model_data["weights"]
    
    return net.predict(img_flat)

if __name__ == "__main__":
    predict()