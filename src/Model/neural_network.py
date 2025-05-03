#libraries
import numpy as np
import random

"""
Basic class for a neural network for recognizing handwritten digits.
"""

#sigmoid function
def sigmoid(z):
    return 1/(1+np.exp(-z))

#derivative of sigmoid function
def sigmoid_prime(z):
    return sigmoid(z)* (1-sigmoid(z))

class Network(object):
    def __init__ (self, sizes):
        self.num_layers = len(sizes)
        self.num_hidden_layers = len(sizes) - 2
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)/np.sqrt(x) for x, y in zip(sizes[:-1], sizes[1:])]
    
    """
    Calculate output. Takes an input vector 'a' of length 784. Outputs the
    final layer of 10 nuerons (0-9) where the greatest number is the 
    predicted answer.
    """
    def predict(self, a):
        return np.argmax(self.feed_forward(a))
    
    def feed_forward(self, a):
        for w, b in zip(self.weights, self.biases):
            a = sigmoid(np.dot(w, a) + b)
        return a
    
    """
    Stochastic Gradient Descent: for each epoch, randomly shuffles the data, and
    splits it into mini batch with specified size. Then repeatedly updates the 
    weights and biases with gradient descent. If test data is provided, it will
    continually check against the test data.
    """
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        if test_data: n_tests = len(test_data)
        n = len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
            mini_batches = [
                training_data[k:k+mini_batch_size] for k in range (0, n, mini_batch_size)
            ]
            for batch in mini_batches:
                self.update_mini_batch(batch, eta)
            if test_data:
                num_correct = self.evaluate(test_data)
                print(f"Epoch {j}. Number correct: {num_correct}/{n_tests}")
            else:
                print(f"Epoch {j}")

    """
    Calculates the backprop for all samples in the mini batch, then
    averages them and subtracts it times eta.
    """
    def update_mini_batch(self, batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in batch:
            delta_nabla_b, delta_nabla_w = self.calculate_backprop(x, y)
            #Sum gradients over mini_batch.
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.biases = [first - (eta / len(batch)) * update for first, update in zip(self.biases, nabla_b)]
        self.weights = [first - (eta/len(batch)) * update for first, update in zip(self.weights, nabla_w)]
    
    """
    Calculate the backprop gradient for a single data point (x being the input and y being the actual)
    """
    def calculate_backprop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        activation = x

        activations = [x] #store activations (after sigmoid) for each layer
        zs = [] #store weighted inputs for each layer
        
        #forward prop
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        
        #backward pass: compute delta for output layer
        delta = self.cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].T)

        for layer in range (2, self.num_layers):
            z = zs[-layer]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-layer+1].T, delta) * sp
            nabla_b[-layer] = delta
            nabla_w[-layer] = np.dot(delta, activations[-layer-1].T)
        return (nabla_b, nabla_w)

    """
    Calculate the cost derivative by simply subtracting y from the output activations
    """
    def cost_derivative(self, output_activations, y):
        return output_activations - y

    """
    Calculate the number out of the test data that was correct at each iteration -- can be
    used to visualize the model learning. 
    """
    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feed_forward(x)), y) for (x, y) in test_data]

        return sum(int(x==y) for (x, y) in test_results)







