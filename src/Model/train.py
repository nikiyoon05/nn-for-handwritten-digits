from neural_network import Network
from load_data import data_loader_wrapper 
from data_loader2 import load_data
import pickle



def main():
    # Load MNIST data
     #training_data, validation_data, test_data = data_loader_wrapper()

    training_data, test_data = load_data()

    # Initialize the network with 784 input neurons, hidden neurons, and 10 output neurons.
    net = Network([784, 100, 10])

    """
    Train the network:
       - epochs: number of times to go over the training data (e.g., 30 epochs)
       - mini_batch_size: number of samples per mini-batch (e.g., 10)
       - eta: learning rate (e.g., 3.0)
    """
    net.SGD(training_data, epochs=15, mini_batch_size=9, eta=3.0, test_data=test_data)

    """
    Save the model parameters using pickle
    Saved to "saved_model.pkl"
    """
    with open("saved_model.pkl", "wb") as f:
        pickle.dump({
            "sizes": net.sizes,
            "weights": net.weights,
            "biases": net.biases
        }, f)

if __name__ == "__main__":
    main()