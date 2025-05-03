"""
Load the MNIST data. Downloaded from kaggle: https://www.kaggle.com/datasets/hojjatk/mnist-dataset
"""
#libraries
import pickle
import gzip
import numpy as np


"""
Returns the MNIST data.
Returns 'train_data', 'validation_data', 'test_data'
Returns as a tuple containing training data, validation data, test data. 

'train_data'is returned as tuple with two entries: numpy ndarray with 
50,000 entires. Each entry is a ndarray with 784 entries, representing a 
28x28 pixel grid. The second entry in training data is a numpy ndarray 
with 50,000 entries. Those entries are the actual lsabeled digit values
from 0 to 9 of the images in the tuple. 

'validation_data' are the same, but with 10,000 each


"""
def data_loader():
    f = gzip.open('data/mnist_expanded.pkl.gz')
    training_data, validation_data, test_data = pickle.load(f, encoding='latin1')
    return training_data, validation_data, test_data

"""
Converts the label of each image for the training data into a 10d vector
with a 1.0 in the jth entry, where j is the actual data.

For the test/validation data, the label is simply an integer, not a vector.
This is done for simplicity in creating a neural network with the train data.
"""
def data_loader_wrapper():
    tr_data, va_data, te_data = data_loader()

    training_inputs  = [np.reshape(x, (784, 1)) for x in tr_data[0]]
    training_results = [vectorized_result(y)     for y in tr_data[1]]

    validation_inputs  = [np.reshape(x, (784, 1)) for x in va_data[0]]
    validation_results = list(va_data[1])               # no one‑hot yet

    test_inputs = [np.reshape(x, (784, 1)) for x in te_data[0]]

    training_data   = list(zip(training_inputs,   training_results))
    validation_data = list(zip(validation_inputs, validation_results))
    test_data       = list(zip(test_inputs,       te_data[1]))

    return training_data, validation_data, test_data

"""
10 dimensional unit vector with 1.0 in jth position and 0's everywhere
else. 
"""
def vectorized_result(j):
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e