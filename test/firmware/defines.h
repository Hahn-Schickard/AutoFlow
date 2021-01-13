#ifndef DEFINES_H_
#define DEFINES_H_

#include "ap_int.h"
#include "ap_fixed.h"

//hls-fpga-machine-learning insert numbers
#define N_INPUT_1_1 28
#define N_INPUT_2_1 28
#define N_INPUT_3_1 1
#define N_INPUT_1_2 28
#define N_INPUT_2_2 28
#define N_INPUT_3_2 1
#define OUT_HEIGHT_3 26
#define OUT_WIDTH_3 26
#define N_FILT_3 32
#define OUT_HEIGHT_5 24
#define OUT_WIDTH_5 24
#define N_FILT_5 32
#define OUT_HEIGHT_7 12
#define OUT_WIDTH_7 12
#define N_FILT_7 32
#define OUT_HEIGHT_8 10
#define OUT_WIDTH_8 10
#define N_FILT_8 64
#define OUT_HEIGHT_10 8
#define OUT_WIDTH_10 8
#define N_FILT_10 64
#define OUT_HEIGHT_12 4
#define OUT_WIDTH_12 4
#define N_FILT_12 64
#define N_LAYER_13 64
#define N_LAYER_15 36

//hls-fpga-machine-learning insert layer-precision
typedef ap_fixed<16,6> model_default_t;
typedef ap_fixed<16,6> input_t;
typedef ap_fixed<16,6> input2_t;
typedef ap_fixed<16,6> layer3_t;
typedef ap_fixed<16,6> layer4_t;
typedef ap_fixed<16,6> layer5_t;
typedef ap_fixed<16,6> layer6_t;
typedef ap_fixed<16,6> layer7_t;
typedef ap_fixed<16,6> layer8_t;
typedef ap_fixed<16,6> layer9_t;
typedef ap_fixed<16,6> layer10_t;
typedef ap_fixed<16,6> layer11_t;
typedef ap_fixed<16,6> layer12_t;
typedef ap_fixed<16,6> layer13_t;
typedef ap_fixed<16,6> layer14_t;
typedef ap_fixed<16,6> layer15_t;
typedef ap_fixed<16,6> result_t;

#endif
