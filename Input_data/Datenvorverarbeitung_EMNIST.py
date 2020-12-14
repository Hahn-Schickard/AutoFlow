import numpy as np
import pathlib

def get_data():    
    path = str(pathlib.Path(__file__).parent.absolute())
    print(path)

    mnist_train_x = np.load("/home/jetson/automatic/Input_data/EMNIST_Data/MNIST/mnist_train_x.npy")
    mnist_train_y = np.load("/home/jetson/automatic/Input_data/EMNIST_Data/MNIST/mnist_train_y.npy")
    mnist_test_x = np.load("/home/jetson/automatic/Input_data/EMNIST_Data/MNIST/mnist_test_x.npy")
    mnist_test_y = np.load("/home/jetson/automatic/Input_data/EMNIST_Data/MNIST/mnist_test_y.npy")
    letter_label_placeholder_train = np.zeros((mnist_train_y.shape[0],26))
    letter_label_placeholder_test = np.zeros((mnist_test_y.shape[0],26))
    
    mnist_train_y = np.concatenate((mnist_train_y, letter_label_placeholder_train), axis=1)
    mnist_test_y = np.concatenate((mnist_test_y, letter_label_placeholder_test), axis=1)
    
    
    letter_train_x = np.load("/home/jetson/automatic/Input_data/EMNIST_Data/Letter/letter_train_x.npy")
    letter_train_y = np.load("/home/jetson/automatic/Input_data/EMNIST_Data/Letter/letter_train_y.npy")
    letter_test_x = np.load("/home/jetson/automatic/Input_data/EMNIST_Data/Letter/letter_test_x.npy")
    letter_test_y = np.load("/home/jetson/automatic/Input_data/EMNIST_Data/Letter/letter_test_y.npy")
    mnist_label_placeholder_train = np.zeros((letter_train_y.shape[0],10))
    mnist_label_placeholder_test = np.zeros((letter_test_y.shape[0],10))
    
    letter_train_y = np.concatenate((mnist_label_placeholder_train, letter_train_y), axis=1)
    letter_test_y = np.concatenate((mnist_label_placeholder_test, letter_test_y), axis=1)
    
    x_train = np.concatenate((mnist_train_x, letter_train_x), axis=0)
    x_test = np.concatenate((mnist_test_x, letter_test_x), axis=0)
    
    x_train = x_train*0.5+0.5
    x_test = x_test*0.5+0.5
    
    y_train = np.concatenate((mnist_train_y, letter_train_y), axis=0)
    y_test = np.concatenate((mnist_test_y, letter_test_y), axis=0)
    
    
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    
    return x_train, y_train, x_test, y_test

    
