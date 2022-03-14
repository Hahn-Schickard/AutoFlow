/* Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: GPL-3.0
============================================================================*/

// This is a standard TensorFlow Lite model file that has been converted into a
// C data array, so it can be easily compiled into a binary for devices that
// don't have a file system.

#ifndef TENSORFLOW_LITE_MODEL_DATA_H_
#define TENSORFLOW_LITE_MODEL_DATA_H_

extern const unsigned char MNIST_tflite[];
extern const int MNIST_tflite_len;

#endif