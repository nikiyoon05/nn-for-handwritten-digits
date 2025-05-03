from neural_network import Network
import pickle
from PIL import Image
import numpy as np
from PIL import ImageOps

def predict():
    with open("saved_model.pkl", "rb") as f:
        model_data = pickle.load(f)

    net = Network(model_data["sizes"])
    net.biases = model_data["biases"]
    net.weights = model_data["weights"]

    img = Image.open("sample_images/6.jpg")
    img_adjusted = img.convert("L").resize((28, 28))
    img_adjusted = ImageOps.invert(img_adjusted)
    
    img_adjusted.save("processed_img.png")

    img_array = np.array(img_adjusted).astype(np.float32)/255.0
    img_flat = img_array.reshape(784, 1)

    prediction = net.predict(img_flat)

    print("Predicted digit:", prediction)   

#Returns a preprocessed image (grayscale, 28x28 stored in a 784 x 1 vector)
def predictNum(img_flat):
    with open("../saved_model.pkl", "rb") as f:
        model_data = pickle.load(f)

    net = Network(model_data["sizes"])
    net.biases = model_data["biases"]
    net.weights = model_data["weights"]
    prediction = net.predict(img_flat)
    return prediction

if __name__ == "__main__":
    predict()