from tensorflow import lite
import tensorflow as tf
import sys
import os

def convert_model_to_tflite(Keras_model_dir, converted_model_dir, model_name, opti, datascript_path):
    """
    A keras model get's converter into a TensorFlow lite model.
    
    Args: 
        Keras_model_dir: Path of the keras model
        converted_model_dir: Path where the converted TensorFlow Lite model should be stored
        model_name: Name of converted .tflite file
            
    Return: 
        model_input_shape: Shape of the inputdata of the model
        model_input_dtype: Dtype of the inputdata of the model
        model_output_neurons: Number of neurons in the output layer
    """
    
    keras_file = Keras_model_dir
    keras_file = tf.keras.models.load_model(keras_file)
    model_input_shape = keras_file.input.shape
    model_input_dtype = keras_file.input.dtype
    model_output_neurons = keras_file.layers[-1].output_shape[1]
    converter = lite.TFLiteConverter.from_keras_model(keras_file)

    if "Quantization" in opti:
        sys.path.append(os.path.dirname(datascript_path))
        datascript = __import__(os.path.splitext(os.path.basename(datascript_path))[0])
        global x_train
        x_train, _, _, _ = datascript.get_data()
        x_train = tf.cast(x_train, tf.float32)
        x_train = tf.data.Dataset.from_tensor_slices(x_train).batch(1)

        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        converter.representative_dataset = representative_dataset
        converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
        converter.inference_input_type = tf.int8  # or tf.uint8
        converter.inference_output_type = tf.int8  # or tf.uint8
        
    tflite_model = converter.convert()
    open(converted_model_dir + model_name + ".tflite", "wb").write(tflite_model)
    return model_input_shape, model_input_dtype, model_output_neurons

def representative_dataset():
    for input_value in x_train.take(250):
        # Model has only one input so each data point has one element.
        yield [input_value]

def convert_model_to_cpp(converted_model_dir, model_name, project_dir):
    """
    A TensorFlow lite model get's converter into a C++ model.
    
    Args: 
        converted_model_dir: Path of the .tflite model
        model_name: Name of the model
        project_dir: Directory of the project where the C++ model should be stored
            
    Return: 
        ---
    """
    
    with open(converted_model_dir + model_name + '.tflite', 'rb') as f:
        content = f.read().hex()
        result = bytearray.fromhex(content)
        with open(project_dir + "/src/" + model_name + "_data.cc", "wb") as w:
            i = 0
            num_values = 0
            
            w.write(bytearray('#include "./../inc/' + model_name + '_data.h"\n'
                              "\n"
                              "// We need to keep the data array aligned on some architectures.\n"
                              "#ifdef __has_attribute\n"
                              "#define HAVE_ATTRIBUTE(x) __has_attribute(x)\n"
                              "#else\n"
                              "#define HAVE_ATTRIBUTE(x) 0\n"
                              "#endif\n"
                              "#if HAVE_ATTRIBUTE(aligned) || (defined(__GNUC__) && !defined(__clang__))\n"
                              "#define DATA_ALIGN_ATTRIBUTE __attribute__((aligned(4)))\n"
                              "#define DATA_ALIGN_ATTRIBUTE __attribute__((aligned(4)))\n"
                              "#else\n"
                              "#define DATA_ALIGN_ATTRIBUTE\n"
                              "#endif\n"
                              "\n"

                              "const unsigned char " + model_name + "_tflite[] DATA_ALIGN_ATTRIBUTE = {\n    ", 'utf-8'))
            
            for value in result:
                num_values+=1
                i+=1
                value = "0x{:02x}".format(value)
                
                if i ==1:
                    w.write(bytearray(value, 'utf-8'))
                elif i == 12:
                    w.write(bytearray(", " + str(value) + ",\n    ", 'utf-8'))
                    i = 0
                else:
                    w.write(bytearray(', ' + str(value), 'utf-8'))
                    
            w.write(bytearray("};\nconst int " + model_name + "_tflite_len = " + str(num_values) + ";", 'utf-8'))
            
            
    with open(project_dir + "/inc/" + model_name + "_data.h", "w") as f:
        f.write('// This is a standard TensorFlow Lite model file that has been converted into a\n'
                '// C data array, so it can be easily compiled into a binary for devices that\n'
                "// don't have a file system.\n"
                '\n'
                '#ifndef TENSORFLOW_LITE_MODEL_DATA_H_\n'
                '#define TENSORFLOW_LITE_MODEL_DATA_H_\n'
                '\n'
                'extern const unsigned char ' + model_name + '_tflite[];\n'
                'extern const int ' + model_name + '_tflite_len;\n'
                '\n'
                '#endif')
