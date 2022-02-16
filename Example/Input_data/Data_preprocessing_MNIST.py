import numpy as np
from tensorflow.keras.datasets import mnist

def get_data():    
    (x_train, y_train), (x_test, y_test) = mnist.load_data()    
    
    x_train = x_train.astype('float32')/255.0
    x_test = x_test.astype('float32')/255.0
    
    return x_train, y_train, x_test, y_test