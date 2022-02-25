''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import os
import shutil
import pathlib


def create_project_dir(project_name, output_path, target):
    """
    Creates a directory where all files of the project will be stored.
    
    Args: 
        project_name:        Name of the project which should be generated
        output_path:         Directory where the project should be generated
        target:              Target to execute the neural network
            
    Return: 
        project_dir: Path of the project directory
    """
    path = output_path
    project_dir = path + "/" + project_name
    
    if not os.path.exists(path):
        os.mkdir(path)

    if not os.path.exists(project_dir):
        os.mkdir(project_dir)
        if "uC" in target:
            os.mkdir(project_dir + "/src")
            os.mkdir(project_dir + "/inc")
        
    return project_dir


def main_functions(project_dir, model_name, model_input_neurons, model_output_neurons, quant_dtype, model_memory):
    """
    The script which loads and executes the model is created
    
    Args: 
        project_dir:          Path of the project directory where the file should be created
        model_name:           Name of the model
        model_input_neurons:  Number of neurons in the input layer of the model
        model_output_neurons: Number of neurons in the output layer of the model
        quant_dtype:          Data type to quantize to
        model_memory:         Preallocate a certain amount of memory for input, 
                              output, and intermediate arrays in kilobytes
    """        
    with open(project_dir + "/src/TF_Lite_exe.cpp", "w") as f:
            
        f.write('#include "TF_Lite_exe.h"\n'
                '\n'
                'namespace {\n'
                '// Create an area of memory to use for input, output, and intermediate arrays.\n'
                'constexpr int kTensorArenaSize = ' + str(model_memory) + ' * 1024;\n'
                'uint8_t tensor_arena[kTensorArenaSize];\n'
                '\n' 'tflite::ErrorReporter* error_reporter = nullptr;\n'
                'const tflite::Model* model = nullptr;\n'
                'tflite::MicroInterpreter* interpreter = nullptr;\n'
                'TfLiteTensor* input = nullptr;\n'
                'TfLiteTensor* output = nullptr;\n'
                '\n')
        if model_output_neurons == 1:
            if quant_dtype is not None and "int8 only" in quant_dtype: 
                f.write('int8_t prediction;\n')
            else:
                f.write('float prediction;\n')
        else:
            if quant_dtype is not None and "int8 only" in quant_dtype: 
                f.write('int8_t* prediction = new int8_t[' + str(model_output_neurons) + '];\n')
            else:
                f.write('float* prediction = new float[' + str(model_output_neurons) + '];\n')
        f.write('}\n'
                '\n'
                'void setup_model() {\n'
                '  static tflite::MicroErrorReporter micro_error_reporter;\n'
                '  error_reporter = &micro_error_reporter;\n'
                '\n'
                "  // Load the tflite Model\n"
                '  model = tflite::GetModel(' + model_name + '_tflite);\n'
                '  if (model->version() != TFLITE_SCHEMA_VERSION) {\n'
                '    error_reporter->Report(\n'
                '        "Model provided is schema version %d not equal "\n'
                '        "to supported version %d.",\n'
                '        model->version(), TFLITE_SCHEMA_VERSION);\n'
                '    return;\n'
                '  }\n'
                '\n'
                '  // This pulls in all the operation implementations we need.\n'
                '  static tflite::AllOpsResolver resolver;\n'
                '\n'
                '  // Build an interpreter to run the model with.\n'
                '  static tflite::MicroInterpreter static_interpreter(\n'
                '      model, resolver, tensor_arena, kTensorArenaSize, error_reporter);\n'
                '  interpreter = &static_interpreter;\n'
                '\n'
                "  // Allocate memory from the tensor_arena for the model's tensors.\n"
                '  TfLiteStatus allocate_status = interpreter->AllocateTensors();\n'
                '  if (allocate_status != kTfLiteOk) {\n'
                '    error_reporter->Report("AllocateTensors() failed");\n'
                '    return;\n'
                '  }\n'
                '\n'
                "  // Obtain pointers to the model's input and output tensors.\n"
                '  input = interpreter->input(0);\n'
                '  output = interpreter->output(0);\n'
                '\n'
                '}\n'
                '\n')
        if model_output_neurons == 1:
            if quant_dtype is not None and "int8 only" in quant_dtype: 
                f.write('int8_t model_execute(int8_t *input_data) {\n'
                        '  for (int i = 0; i < ' + str(model_input_neurons) + '; ++i) {\n'
                        '    input->data.int8[i] = *input_data;\n')
            else:
                f.write('float model_execute(float *input_data) {\n'
                        '  for (int i = 0; i < ' + str(model_input_neurons) + '; ++i) {\n'
                        '    input->data.f[i] = *input_data;\n')
        else:
            if quant_dtype is not None and "int8 only" in quant_dtype: 
                f.write('int8_t* model_execute(int8_t *input_data) {\n'
                        '  for (int i = 0; i < ' + str(model_input_neurons) + '; ++i) {\n'
                        '    input->data.int8[i] = *input_data;\n')
            else:
                f.write('float* model_execute(float *input_data) {\n'
                        '  for (int i = 0; i < ' + str(model_input_neurons) + '; ++i) {\n'
                        '    input->data.f[i] = *input_data;\n')
        f.write('    input_data++;\n'
                '  }\n'
                '\n'
                '  // Run inference, and report any error\n'
                '  TfLiteStatus invoke_status = interpreter->Invoke();\n'
                '  if (invoke_status != kTfLiteOk) {\n'
                '    error_reporter->Report("Error by invoking interpreter'r"\n"'");\n'
                '    return 0;\n'
                '  }\n'
                '\n'
                "  // Read the prediction from the model's output tensor\n")
        if model_output_neurons == 1:
            if quant_dtype is not None and "int8 only" in quant_dtype: 
                f.write('    prediction = output->data.int8[0];\n')
            else:
                f.write('    prediction = output->data.f[0];\n')
        else:
            f.write('  for (int i = 0; i < ' + str(model_output_neurons) + '; i++) {\n')
            if quant_dtype is not None and "int8 only" in quant_dtype: 
                f.write('    prediction[i] = output->data.int8[i];\n')
            else:
                f.write('    prediction[i] = output->data.f[i];\n')
            f.write('  }\n')
        f.write('\n'
                '  return prediction;\n'
                '}\n')
                
                          
    with open(project_dir + "/inc/TF_Lite_exe.h", "w") as f:
        f.write('#include "' + str(model_name) + '_data.h"\n'
                '#include "tensorflow/lite/micro/all_ops_resolver.h"\n'
                '#include "tensorflow/lite/micro/micro_error_reporter.h"\n'
                '#include "tensorflow/lite/micro/micro_interpreter.h"\n'
                '#include "tensorflow/lite/schema/schema_generated.h"\n'
                '#include "tensorflow/lite/version.h"\n'
                '\n'
                'void setup_model();\n')
        if model_output_neurons == 1:
            if quant_dtype is not None and "int8 only" in quant_dtype: 
                f.write('int8_t model_execute(int8_t *);')
            else:
                f.write('float model_execute(float *);')
        else:
            if quant_dtype is not None and "int8 only" in quant_dtype: 
                f.write('int8_t* model_execute(int8_t *);')
            else:
                f.write('float* model_execute(float *);')
        

def TensorFlow_library(project_dir):
    """
    Creates the TensorFlow library with all necessary files in the project directory.
    
    Args: 
        project_dir: Path of the project directory where the file should be created
    """    
    shutil.copytree(str(pathlib.Path(__file__).parent.absolute()) + "/TensorFlow_library", project_dir + "/TensorFlow_library")


def pruned_keras_model(keras_model_dir, project_dir, model_name):
    """
    Copies the pruned keras model into the project directory.
    
    Args: 
        keras_model_dir: Path of the keras model
        project_dir:     Path of the project directory where the file should be created
        model_name:      Name of the keras model
    """
    shutil.copy(keras_model_dir, project_dir + "/" + model_name + ".h5")