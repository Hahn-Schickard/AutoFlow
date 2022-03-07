import tensorflow as tf
import numpy as np
import sys
sys.path.insert(1, '..')
from data.data_preprocessing_mnist import get_data


# Path of TFLite model
tflite_model_file = '../data/mnist_model.tflite'
# Get data to test the model
_, _, x_test, y_test = get_data()

# Read the data of your TFLite model file
with open(tflite_model_file, 'rb') as f:
    tflite_model = f.read()
    
# Load TFLite model and allocate tensors
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

# Get input and output of model
input = interpreter.get_input_details()[0]
output = interpreter.get_output_details()[0]

# If you quantized your model to int8 only you have 
# convert your input data as int8 values
# x_test = x_test.astype(np.int8)

# Gather the results for the test data
predictions = []
for sample in x_test:
    # Set input data
    interpreter.set_tensor(input['index'], sample)
    # Run the model
    interpreter.invoke()
    # Get model output
    pred = interpreter.get_tensor(output['index'])
    predictions.append(pred.argmax())

model_acc = sum(1 for a,b in zip(predictions,y_test) if a == b) / len(predictions)

print('Model accuracy: {:.2f}%'.format(model_acc*100))