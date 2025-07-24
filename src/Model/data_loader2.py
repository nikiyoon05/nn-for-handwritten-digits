#libraries
import pickle
import gzip
import numpy as np
import struct
import os

def load_images(filename):
    with open(filename, 'rb') as f:
        magic, num, rows, cols = struct.unpack(">IIII", f.read(16))
        data = np.frombuffer(f.read(), dtype=np.uint8)
        return data.reshape(num, rows * cols)  # Flatten 28x28 to 784

def load_labels(filename):
    with open(filename, 'rb') as f:
        magic, num = struct.unpack(">II", f.read(8))
        return np.frombuffer(f.read(), dtype=np.uint8)

def load_data(path="data/"):
    # Load raw data
    train_images = load_images(os.path.join(path, "train-images.idx3-ubyte"))
    train_labels = load_labels(os.path.join(path, "train-labels.idx1-ubyte"))
    test_images = load_images(os.path.join(path, "t10k-images.idx3-ubyte"))
    test_labels = load_labels(os.path.join(path, "t10k-labels.idx1-ubyte"))

    # Normalize pixel values to [0, 1]
    train_images = train_images.astype(np.float32) / 255.0
    test_images = test_images.astype(np.float32) / 255.0

   # Reshape inputs to column vectors
    train_inputs = [x.reshape(784, 1) for x in train_images]
    test_inputs = [x.reshape(784, 1) for x in test_images]

    # One-hot encode labels for training
    def vectorized_result(j):
        e = np.zeros((10, 1))
        e[j] = 1.0
        return e

    train_labels_vec = [vectorized_result(y) for y in train_labels]

    # Zip images with labels
    training_data = list(zip(train_inputs, train_labels_vec))
    test_data = list(zip(test_inputs, test_labels))

    return training_data, test_data