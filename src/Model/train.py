"""
Train a neural network on digit data and save the trained model.
Dependencies:
 - "neural_network.py"
 - "data_loader2.py:
 - pickle
"""

from neural_network import Network
from data_loader2 import load_data
import pickle

def main():
    # Load training and test data (should be formatted as (x, y) pairs)
    training_data, test_data = load_data()

    # Initialize the neural net: 
    # 784 inputs (28x28 image), 100 hidden neurons, 10 output classes (digits 0–9)
    net = Network([784, 100, 10])

    # Train the network using stochastic gradient descent
    # Params: epochs, mini-batch size, learning rate
    net.SGD(
        training_data, 
        epochs=15, 
        mini_batch_size=9, 
        eta=3.0, 
        test_data=test_data
    )

    # Save the trained model so we can reuse it later without retraining
    with open("saved_model.pkl", "wb") as f:
        pickle.dump({
            "sizes": net.sizes,
            "weights": net.weights,
            "biases": net.biases
        }, f)

if __name__ == "__main__":
    main()
