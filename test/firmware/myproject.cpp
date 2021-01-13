//
//    rfnoc-hls-neuralnet: Vivado HLS code for neural-net building blocks
//
//    Copyright (C) 2017 EJ Kreinar
//
//    This program is free software: you can redistribute it and/or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation, either version 3 of the License, or
//    (at your option) any later version.
//
//    This program is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU General Public License for more details.
//
//    You should have received a copy of the GNU General Public License
//    along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
#include <iostream>

#include "myproject.h"
#include "parameters.h"

void myproject(
    input_t input1[N_INPUT_1_1*N_INPUT_2_1*N_INPUT_3_1],
    result_t layer17_out[N_LAYER_15],
    unsigned short &const_size_in_1,
    unsigned short &const_size_out_1
) {

    //hls-fpga-machine-learning insert IO
    #pragma HLS ARRAY_RESHAPE variable=input1 complete dim=0
    #pragma HLS ARRAY_PARTITION variable=layer17_out complete dim=0
    #pragma HLS INTERFACE ap_vld port=input1,layer17_out 
    #pragma HLS PIPELINE 

    const_size_in_1 = N_INPUT_1_1*N_INPUT_2_1*N_INPUT_3_1;
    const_size_out_1 = N_LAYER_15;

#ifndef __SYNTHESIS__
    static bool loaded_weights = false;
    if (!loaded_weights) {
        //hls-fpga-machine-learning insert load weights
        nnet::load_weights_from_txt<model_default_t, 288>(w3, "w3.txt");
        nnet::load_weights_from_txt<model_default_t, 32>(b3, "b3.txt");
        nnet::load_weights_from_txt<model_default_t, 9216>(w5, "w5.txt");
        nnet::load_weights_from_txt<model_default_t, 32>(b5, "b5.txt");
        nnet::load_weights_from_txt<model_default_t, 18432>(w8, "w8.txt");
        nnet::load_weights_from_txt<model_default_t, 64>(b8, "b8.txt");
        nnet::load_weights_from_txt<model_default_t, 36864>(w10, "w10.txt");
        nnet::load_weights_from_txt<model_default_t, 64>(b10, "b10.txt");
        nnet::load_weights_from_txt<model_default_t, 65536>(w13, "w13.txt");
        nnet::load_weights_from_txt<model_default_t, 64>(b13, "b13.txt");
        nnet::load_weights_from_txt<model_default_t, 2304>(w15, "w15.txt");
        nnet::load_weights_from_txt<model_default_t, 36>(b15, "b15.txt");
        loaded_weights = true;
    }
#endif

    // ****************************************
    // NETWORK INSTANTIATION
    // ****************************************

    //hls-fpga-machine-learning insert layers

    input2_t conv2d_95_input[N_INPUT_1_2*N_INPUT_2_2*N_INPUT_3_2];
    #pragma HLS ARRAY_PARTITION variable=conv2d_95_input complete dim=0
    layer3_t layer3_out[OUT_HEIGHT_3*OUT_WIDTH_3*N_FILT_3];
    #pragma HLS ARRAY_PARTITION variable=layer3_out complete dim=0
    nnet::conv_2d_latency_cl<input2_t, layer3_t, config3>(conv2d_95_input, layer3_out, w3, b3);

    layer4_t layer4_out[OUT_HEIGHT_3*OUT_WIDTH_3*N_FILT_3];
    #pragma HLS ARRAY_PARTITION variable=layer4_out complete dim=0
    nnet::relu<layer3_t, layer4_t, relu_config4>(layer3_out, layer4_out);

    layer5_t layer5_out[OUT_HEIGHT_5*OUT_WIDTH_5*N_FILT_5];
    #pragma HLS ARRAY_PARTITION variable=layer5_out complete dim=0
    nnet::conv_2d_latency_cl<layer4_t, layer5_t, config5>(layer4_out, layer5_out, w5, b5);

    layer6_t layer6_out[OUT_HEIGHT_5*OUT_WIDTH_5*N_FILT_5];
    #pragma HLS ARRAY_PARTITION variable=layer6_out complete dim=0
    nnet::relu<layer5_t, layer6_t, relu_config6>(layer5_out, layer6_out);

    layer7_t layer7_out[OUT_HEIGHT_7*OUT_WIDTH_7*N_FILT_7];
    #pragma HLS ARRAY_PARTITION variable=layer7_out complete dim=0
    nnet::pooling2d_cl<layer6_t, config7>(layer6_out, layer7_out);

    layer8_t layer8_out[OUT_HEIGHT_8*OUT_WIDTH_8*N_FILT_8];
    #pragma HLS ARRAY_PARTITION variable=layer8_out complete dim=0
    nnet::conv_2d_latency_cl<layer7_t, layer8_t, config8>(layer7_out, layer8_out, w8, b8);

    layer9_t layer9_out[OUT_HEIGHT_8*OUT_WIDTH_8*N_FILT_8];
    #pragma HLS ARRAY_PARTITION variable=layer9_out complete dim=0
    nnet::relu<layer8_t, layer9_t, relu_config9>(layer8_out, layer9_out);

    layer10_t layer10_out[OUT_HEIGHT_10*OUT_WIDTH_10*N_FILT_10];
    #pragma HLS ARRAY_PARTITION variable=layer10_out complete dim=0
    nnet::conv_2d_latency_cl<layer9_t, layer10_t, config10>(layer9_out, layer10_out, w10, b10);

    layer11_t layer11_out[OUT_HEIGHT_10*OUT_WIDTH_10*N_FILT_10];
    #pragma HLS ARRAY_PARTITION variable=layer11_out complete dim=0
    nnet::relu<layer10_t, layer11_t, relu_config11>(layer10_out, layer11_out);

    layer12_t layer12_out[OUT_HEIGHT_12*OUT_WIDTH_12*N_FILT_12];
    #pragma HLS ARRAY_PARTITION variable=layer12_out complete dim=0
    nnet::pooling2d_cl<layer11_t, config12>(layer11_out, layer12_out);

    layer13_t layer13_out[N_LAYER_13];
    #pragma HLS ARRAY_PARTITION variable=layer13_out complete dim=0
    nnet::dense_latency<layer12_t, layer13_t, config13>(layer12_out, layer13_out, w13, b13);

    layer14_t layer14_out[N_LAYER_13];
    #pragma HLS ARRAY_PARTITION variable=layer14_out complete dim=0
    nnet::relu<layer13_t, layer14_t, relu_config14>(layer13_out, layer14_out);

    layer15_t layer15_out[N_LAYER_15];
    #pragma HLS ARRAY_PARTITION variable=layer15_out complete dim=0
    nnet::dense_latency<layer14_t, layer15_t, config15>(layer14_out, layer15_out, w15, b15);

    nnet::softmax<layer15_t, result_t, softmax_config17>(layer15_out, layer17_out);

}
