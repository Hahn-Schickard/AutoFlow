import os
import sys
import ntpath
import pathlib

from Auto_TF_to_uC.convert_keras_to_cc import *
from Auto_TF_to_uC.write_files_uc import *

def convert_and_write(Keras_model_dir, project_name, output_path, optimizations, datascript_path):  
    """
    A keras model get's converted into a C++ model, the project directory is created
    and all files that are needed to compile the project get generated.
    
    Args: 
        Keras_model_dir: Path of the keras model
        project_name: Name of the project which should be generated
        output_path: Directory where the project should be generated
            
    Return: 
        ---
    """   
    
    converted_model_dir = str(pathlib.Path(__file__).parent.absolute()) + "/Converted_model_files/"
    model_name = ntpath.basename(Keras_model_dir)
    model_name,_ = os.path.splitext(model_name)
    model_input_neurons = 1
    
    project_dir = create_project_dir(project_name, output_path)
    
    
    model_input_shape, model_input_dtype, model_output_neurons = convert_model_to_tflite(Keras_model_dir, converted_model_dir, model_name, optimizations, datascript_path)
    convert_model_to_cpp(converted_model_dir, model_name, project_dir)
    
    for i in range(1,len(model_input_shape)):
        model_input_neurons = model_input_neurons * model_input_shape[i]
    
    
    main_functions(project_dir, model_name, model_input_neurons, model_output_neurons, model_input_dtype, model_input_shape, len(model_input_shape))
    TensorFlow_library(project_dir)
