#include "./../inc/CIFAR10_model_data.h"
#include "./../../../TensorFlow_library/tensorflow/lite/experimental/micro/kernels/all_ops_resolver.h"
#include "./../../../TensorFlow_library/tensorflow/lite/experimental/micro/micro_error_reporter.h"
#include "./../../../TensorFlow_library/tensorflow/lite/experimental/micro/micro_interpreter.h"
#include "./../../../TensorFlow_library/tensorflow/lite/schema/schema_generated.h"
#include "./../../../TensorFlow_library/tensorflow/lite/version.h"

namespace {
// Create an area of memory to use for input, output, and intermediate arrays.
constexpr int kTensorArenaSize = 170 * 1024;
uint8_t tensor_arena[kTensorArenaSize];

tflite::ErrorReporter* error_reporter = nullptr;
const tflite::Model* model = nullptr;
tflite::MicroInterpreter* interpreter = nullptr;
TfLiteTensor* input = nullptr;
TfLiteTensor* output = nullptr;

int input_neurons;
float* prediction = new float[10];
}

void setup() {
  static tflite::MicroErrorReporter micro_error_reporter;
  error_reporter = &micro_error_reporter;

  // Load the tflite Model
  model = tflite::GetModel(CIFAR10_model_tflite);
  if (model->version() != TFLITE_SCHEMA_VERSION) {
    error_reporter->Report(
        "Model provided is schema version %d not equal "
        "to supported version %d.",
        model->version(), TFLITE_SCHEMA_VERSION);
    return;
  }

  // This pulls in all the operation implementations we need.
  static tflite::ops::micro::AllOpsResolver resolver;

  // Build an interpreter to run the model with.
  static tflite::MicroInterpreter static_interpreter(
      model, resolver, tensor_arena, kTensorArenaSize, error_reporter);
  interpreter = &static_interpreter;

  // Allocate memory from the tensor_arena for the model's tensors.
  TfLiteStatus allocate_status = interpreter->AllocateTensors();
  if (allocate_status != kTfLiteOk) {
    error_reporter->Report("AllocateTensors() failed");
    return;
  }

  // Obtain pointers to the model's input and output tensors.
  input = interpreter->input(0);
  output = interpreter->output(0);

}

float* model_execute(float input_data[32][32][3]) { //the inputdata is a parameter
 
  // Place the inputdata in the model's input tensor as one dimensional input.
  // In this case there is an image with three channels and 32x32 pixels. 
  input_neurons = 0;
  for(int i1 = 0; i1 < 32; i1++) {	// i1 = Image height
    for(int i2 = 0; i2 < 32; i2++) {	// i2 = Image width
      for(int i3 = 0; i3 < 3; i3++) {	// i3 = Image channels
        input->data.f[input_neurons] = input_data[i1][i2][i3];
        input_neurons++;
      }
    }
  }

  // Run inference, and report any error
  TfLiteStatus invoke_status = interpreter->Invoke();
  if (invoke_status != kTfLiteOk) {
    error_reporter->Report("Error by invoking interpreter\n");
    return 0;
  }

  // Read the prediction from the model's output tensor
  // In this case the model has 10 different output classes.
  for (int i = 0; i < 10; i++) {
    prediction[i] = output->data.f[i];
  }

  return prediction;

}
