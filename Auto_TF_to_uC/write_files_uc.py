import os
import fileinput
import shutil
import pathlib


def create_project_dir(project_name, output_path):
    """
    Creates a directory where all files of the project will be stored.
    
    Args: 
        project_name: Name of the project which should be generated
        output_path: Directory where the project should be generated
            
    Return: 
        project_dir: Path of the project directory
    """    
    
    path = output_path
    project_dir = path + "/" + project_name
    
    if not os.path.exists(path):
        os.mkdir(path)
        
    if not os.path.exists(project_dir):
        os.mkdir(project_dir)
        os.mkdir(project_dir + "/src")
        os.mkdir(project_dir + "/inc")
        
    return project_dir


def main_functions(project_dir, model_name, model_input_neurons, model_output_neurons, model_input_dtype, model_input_shape, model_input_dim):
    """
    The script which loads and executes the model is created
    
    Args: 
        project_dir: Path of the project directory where the file should be created
        model_name: Name of the model
        model_input_neurons: Number of neurons in the input layer of the model
        model_output_neurons: Number of neurons in the output layer of the model
        model_input_dtype: Dtype of the inputdata of the model
        model_input_shape: Shape of the inputdata of the model
        model_input_dim: Number of dimensions of the inputdata
            
    Return: 
        ---
    """
    if 'float' in str(model_input_dtype):
        in_dt = 'f'
    elif 'TfLiteFloat16' in str(model_input_dtype):
        in_dt = 'f16'
    elif 'TfLiteComplex' in str(model_input_dtype):
        in_dt = 'c64'
    elif 'int64' in str(model_input_dtype):
        in_dt = 'i64'
    elif 'int32' in str(model_input_dtype):
        in_dt = 'i32'
    elif 'int16' in str(model_input_dtype):
        in_dt = 'i16'
    elif 'int8' in str(model_input_dtype):
        in_dt = 'int8'
    elif 'uint8' in str(model_input_dtype):
        in_dt = 'uint8'
    elif 'char' in str(model_input_dtype):
        in_dt = 'raw'
    elif 'const char' in str(model_input_dtype):
        in_dt = 'raw_const'
    elif 'bool' in str(model_input_dtype):
        in_dt = 'b'
    else:
        print("No known datatype of inputdata")
        
    with open(project_dir + "/src/TF_Lite_exe.cc", "w") as f:
            
        f.write('#include "./../inc/TF_Lite_exe.h"\n'
                '\n'
                'namespace {\n'
                '// Create an area of memory to use for input, output, and intermediate arrays.\n'
                'constexpr int kTensorArenaSize = 170 * 1024;\n'
                'uint8_t tensor_arena[kTensorArenaSize];\n'
                '\n' 'tflite::ErrorReporter* error_reporter = nullptr;\n'
                'const tflite::Model* model = nullptr;\n'
                'tflite::MicroInterpreter* interpreter = nullptr;\n'
                'TfLiteTensor* input = nullptr;\n'
                'TfLiteTensor* output = nullptr;\n'
                '\n'
                'int input_neurons;\n'
                'float* prediction = new float[' + str(model_output_neurons) + '];\n'
                '}\n'
                '\n'
                'void setup() {\n'
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
                '  static tflite::ops::micro::AllOpsResolver resolver;\n'
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
                '\n'
                'float* model_execute(float input_data')
        
        for i in range(1,model_input_dim):
            f.write('[' + str(model_input_shape[i]) + ']')
        
        f.write(') {\n'
                "  // Place our inputdata in the model's input tensor as one dimensional input\n"
                '  input_neurons = 0;\n')
        
        for i in range(1,model_input_dim):
            f.write('  for(int i' + str(i) + ' = 0; i' + str(i) + ' < ' + str(model_input_shape[i]) + '; i' + str(i) + '++) {\n')
            
        f.write('  input->data.' + in_dt + '[input_neurons] = input_data[')
        
        for i in range(1,model_input_dim):
            if i == model_input_dim-1:
                f.write('i' + str(i) + '];\n')
            else:
                f.write('i' + str(i) + '][')
        
        f.write('  input_neurons++;\n')
                
        for i in range(model_input_dim-1,0,-1):
            f.write('  }\n')
            
        f.write('\n'
                '  // Run inference, and report any error\n'
                '  TfLiteStatus invoke_status = interpreter->Invoke();\n'
                '  if (invoke_status != kTfLiteOk) {\n'
                '    error_reporter->Report("Error by invoking interpreter'r"\n"'");\n'
                '    return 0;\n'
                '  }\n'
                '\n'
                "  // Read the prediction from the model's output tensor\n"
                '  for (int i = 0; i < ' + str(model_output_neurons) + '; i++) {\n'
                '    prediction[i] = output->data.f[i];\n'
                '  }\n'
                '\n'
                '  return prediction;\n'
                '\n'
                '}\n')
                
                          
    with open(project_dir + "/inc/TF_Lite_exe.h", "w") as f:
        f.write('#include "./inc/' + str(model_name) + '_data.h"\n'
                '#include "./tensorflow/lite/experimental/micro/kernels/all_ops_resolver.h"\n'
                '#include "./tensorflow/lite/experimental/micro/micro_error_reporter.h"\n'
                '#include "./tensorflow/lite/experimental/micro/micro_interpreter.h"\n'
                '#include "./tensorflow/lite/schema/schema_generated.h"\n'
                '#include "./tensorflow/lite/version.h"\n'
                '\n'
                'void setup();\n'
                'float* model_execute(float ')
         
        for i in range(1,model_input_dim):
            f.write('[' + str(model_input_shape[i]) + ']')
        
        f.write(');')
        

def TensorFlow_library(project_dir):
    """
    Creates the TensorFlow library with all necessary files in the project directory.
    
    Args: 
        project_dir: Path of the project directory where the file should be created
            
    Return: 
        ---
    """    
    
    shutil.copytree(str(pathlib.Path(__file__).parent.absolute()) + "/TensorFlow_library", project_dir + "/TensorFlow_library")


def create_project_dir(project_name, output_path):
    """
    Creates a directory where all files of the project will be stored.
    
    Args: 
        project_name: Name of the project which should be generated
        output_path: Directory where the project should be generated
            
    Return: 
        project_dir: Path of the project directory
    """    
    path = output_path
    project_dir = path + "/" + project_name
    
    if not os.path.exists(path):
        os.mkdir(path)
        
    if not os.path.exists(project_dir):
        os.mkdir(project_dir)
        os.mkdir(project_dir + "/src")
        os.mkdir(project_dir + "/inc")
        
    return project_dir