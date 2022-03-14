/* Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: GPL-3.0
============================================================================*/

#include <TensorFlowLite.h>

#include "input_data.h"
#include "Model_output.h"

#include "tf_lite_exe.h"

float* prediction;

char buffer[50];

// The name of this function is important for Arduino compatibility.
void setup() {
  Serial.begin(9600);
  
  setup_model();
}

// The name of this function is important for Arduino compatibility.
void loop() {

  prediction = model_execute(input_img_7);
  for(int i=0; i<10; i++){
    sprintf(buffer, "Prediction %c: %.2f%%\n", pred_labels[i], prediction[i]*100);
    Serial.print(buffer);
  }

}
