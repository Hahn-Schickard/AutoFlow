#include "./TFLite_exe.h"

char pred_labels[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

// Globals, used for compatibility with Arduino-style sketches.
namespace {
tflite::ErrorReporter* error_reporter = nullptr;
const tflite::Model* model = nullptr;
tflite::MicroInterpreter* interpreter = nullptr;
TfLiteTensor* input = nullptr;
TfLiteTensor* output = nullptr;

// Create an area of memory to use for input, output, and intermediate arrays.
// Finding the minimum value for your model may require some trial and error.
constexpr int kTensorArenaSize = 170 * 1024;
uint8_t tensor_arena[kTensorArenaSize];
}  // namespace

// The name of this function is important for Arduino compatibility.

int i=0;
int j=0;

void setup() { 

  // Set up logging. Google style is to avoid globals or statics because of
  // lifetime uncertainty, but since this has a trivial destructor it's okay.
  // NOLINTNEXTLINE(runtime-global-variables)
  static tflite::MicroErrorReporter micro_error_reporter;
  error_reporter = &micro_error_reporter;

  // Map the model into a usable data structure. This doesn't involve any
  // copying or parsing, it's a very lightweight operation.
  model = tflite::GetModel(model_quantized_tflite);
  if (model->version() != TFLITE_SCHEMA_VERSION) {
    error_reporter->Report(
        "Model provided is schema version %d not equal "
        "to supported version %d.",
        model->version(), TFLITE_SCHEMA_VERSION);
    return;
  }

  // This pulls in all the operation implementations we need.
  // NOLINTNEXTLINE(runtime-global-variables)
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


// The name of this function is important for Arduino compatibility.
void model_execute(float *input_im, char *label_pred_1, float *acc_pred_1, char *label_pred_2, float *acc_pred_2, char *label_pred_3, float *acc_pred_3) {

  // Place our calculated x value in the model's input tensor
  for (int i = 0; i < 784; ++i) {
    input->data.f[i] = *input_im;
    input_im++;
  }

  // Run inference, and report any error
  TfLiteStatus invoke_status = interpreter->Invoke();
  if (invoke_status != kTfLiteOk) {
    error_reporter->Report("Invoke failed on x_val: \n");
    return;
  }

  *acc_pred_1 = 0;
  *acc_pred_2 = 0;
  *acc_pred_3 = 0;
  
  for (int i = 0; i < 36; ++i) {
        float current = output->data.f[i];
		error_reporter->Report("Current %d: %f\n", i+1, current);
		if(current > *acc_pred_1) {
      *acc_pred_3 = *acc_pred_2;
			*label_pred_3 = *label_pred_2;

			*acc_pred_2 = *acc_pred_1;
			*label_pred_2 = *label_pred_1;
      
      *acc_pred_1 = current;
			*label_pred_1 = pred_labels[i];
		}
    else if(current > *acc_pred_2) {
      *acc_pred_3 = *acc_pred_2;
			*label_pred_3 = *label_pred_2;
      
      *acc_pred_2 = current;
			*label_pred_2 = pred_labels[i];
		}
    else if(current > *acc_pred_3) {
      *acc_pred_3 = current;
			*label_pred_3 = pred_labels[i];
		}
  }
  
}
