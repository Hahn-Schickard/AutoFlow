#ifndef PARAMETERS_H_
#define PARAMETERS_H_

#include "ap_int.h"
#include "ap_fixed.h"

#include "nnet_utils/nnet_helpers.h"
//hls-fpga-machine-learning insert includes
#include "nnet_utils/nnet_activation.h"
#include "nnet_utils/nnet_conv2d.h"
#include "nnet_utils/nnet_conv2d_large.h"
#include "nnet_utils/nnet_dense.h"
#include "nnet_utils/nnet_dense_compressed.h"
#include "nnet_utils/nnet_dense_large.h"
#include "nnet_utils/nnet_pooling.h"
 
//hls-fpga-machine-learning insert weights
#include "weights/w3.h"
#include "weights/b3.h"
#include "weights/w5.h"
#include "weights/b5.h"
#include "weights/w8.h"
#include "weights/b8.h"
#include "weights/w10.h"
#include "weights/b10.h"
#include "weights/w13.h"
#include "weights/b13.h"
#include "weights/w15.h"
#include "weights/b15.h"

//hls-fpga-machine-learning insert layer-config
struct config3 : nnet::conv2d_config {
    static const unsigned pad_top = 0;
    static const unsigned pad_bottom = 0;
    static const unsigned pad_left = 0;
    static const unsigned pad_right = 0;
    static const unsigned in_height = N_INPUT_1_2;
    static const unsigned in_width = N_INPUT_2_2;
    static const unsigned n_chan = N_INPUT_3_2;
    static const unsigned filt_height = 3;
    static const unsigned filt_width = 3;
    static const unsigned n_filt = N_FILT_3;
    static const unsigned stride_height = 1;
    static const unsigned stride_width = 1;
    static const unsigned out_height = OUT_HEIGHT_3;
    static const unsigned out_width = OUT_WIDTH_3;
    static const unsigned reuse_factor = 1;
    static const unsigned n_zeros = 0;
    static const bool store_weights_in_bram = false;
    typedef ap_fixed<16,6> accum_t;
    typedef model_default_t bias_t;
    typedef model_default_t weight_t;
    typedef std::nullptr_t mult_config;
};

struct relu_config4 : nnet::activ_config {
    static const unsigned n_in = OUT_HEIGHT_3*OUT_WIDTH_3*N_FILT_3;
    static const unsigned table_size = 1024;
    static const unsigned io_type = nnet::io_parallel;
    static const unsigned reuse_factor = 1;
    typedef ap_fixed<18,8> table_t;
};

struct config5 : nnet::conv2d_config {
    static const unsigned pad_top = 0;
    static const unsigned pad_bottom = 0;
    static const unsigned pad_left = 0;
    static const unsigned pad_right = 0;
    static const unsigned in_height = OUT_HEIGHT_3;
    static const unsigned in_width = OUT_WIDTH_3;
    static const unsigned n_chan = N_FILT_3;
    static const unsigned filt_height = 3;
    static const unsigned filt_width = 3;
    static const unsigned n_filt = N_FILT_5;
    static const unsigned stride_height = 1;
    static const unsigned stride_width = 1;
    static const unsigned out_height = OUT_HEIGHT_5;
    static const unsigned out_width = OUT_WIDTH_5;
    static const unsigned reuse_factor = 1;
    static const unsigned n_zeros = 0;
    static const bool store_weights_in_bram = false;
    typedef ap_fixed<16,6> accum_t;
    typedef model_default_t bias_t;
    typedef model_default_t weight_t;
    typedef std::nullptr_t mult_config;
};

struct relu_config6 : nnet::activ_config {
    static const unsigned n_in = OUT_HEIGHT_5*OUT_WIDTH_5*N_FILT_5;
    static const unsigned table_size = 1024;
    static const unsigned io_type = nnet::io_parallel;
    static const unsigned reuse_factor = 1;
    typedef ap_fixed<18,8> table_t;
};

struct config7 : nnet::pooling2d_config {
    static const unsigned in_height = 24;
    static const unsigned in_width = OUT_WIDTH_5;
    static const unsigned n_filt = N_FILT_7;
    static const unsigned stride_height = 2;
    static const unsigned stride_width = 2;
    static const unsigned pool_height = 2;
    static const unsigned pool_width = 2;
    static const unsigned out_height = OUT_HEIGHT_7;
    static const unsigned out_width = OUT_WIDTH_7;
    static const unsigned pad_top = 0;
    static const unsigned pad_bottom = 0;
    static const unsigned pad_left = 0;
    static const unsigned pad_right = 0;
    static const nnet::Pool_Op pool_op = nnet::Max;
    static const unsigned reuse = 1;
};

struct config8 : nnet::conv2d_config {
    static const unsigned pad_top = 0;
    static const unsigned pad_bottom = 0;
    static const unsigned pad_left = 0;
    static const unsigned pad_right = 0;
    static const unsigned in_height = OUT_HEIGHT_7;
    static const unsigned in_width = OUT_WIDTH_7;
    static const unsigned n_chan = N_FILT_7;
    static const unsigned filt_height = 3;
    static const unsigned filt_width = 3;
    static const unsigned n_filt = N_FILT_8;
    static const unsigned stride_height = 1;
    static const unsigned stride_width = 1;
    static const unsigned out_height = OUT_HEIGHT_8;
    static const unsigned out_width = OUT_WIDTH_8;
    static const unsigned reuse_factor = 1;
    static const unsigned n_zeros = 0;
    static const bool store_weights_in_bram = false;
    typedef ap_fixed<16,6> accum_t;
    typedef model_default_t bias_t;
    typedef model_default_t weight_t;
    typedef std::nullptr_t mult_config;
};

struct relu_config9 : nnet::activ_config {
    static const unsigned n_in = OUT_HEIGHT_8*OUT_WIDTH_8*N_FILT_8;
    static const unsigned table_size = 1024;
    static const unsigned io_type = nnet::io_parallel;
    static const unsigned reuse_factor = 1;
    typedef ap_fixed<18,8> table_t;
};

struct config10 : nnet::conv2d_config {
    static const unsigned pad_top = 0;
    static const unsigned pad_bottom = 0;
    static const unsigned pad_left = 0;
    static const unsigned pad_right = 0;
    static const unsigned in_height = OUT_HEIGHT_8;
    static const unsigned in_width = OUT_WIDTH_8;
    static const unsigned n_chan = N_FILT_8;
    static const unsigned filt_height = 3;
    static const unsigned filt_width = 3;
    static const unsigned n_filt = N_FILT_10;
    static const unsigned stride_height = 1;
    static const unsigned stride_width = 1;
    static const unsigned out_height = OUT_HEIGHT_10;
    static const unsigned out_width = OUT_WIDTH_10;
    static const unsigned reuse_factor = 1;
    static const unsigned n_zeros = 0;
    static const bool store_weights_in_bram = false;
    typedef ap_fixed<16,6> accum_t;
    typedef model_default_t bias_t;
    typedef model_default_t weight_t;
    typedef std::nullptr_t mult_config;
};

struct relu_config11 : nnet::activ_config {
    static const unsigned n_in = OUT_HEIGHT_10*OUT_WIDTH_10*N_FILT_10;
    static const unsigned table_size = 1024;
    static const unsigned io_type = nnet::io_parallel;
    static const unsigned reuse_factor = 1;
    typedef ap_fixed<18,8> table_t;
};

struct config12 : nnet::pooling2d_config {
    static const unsigned in_height = 8;
    static const unsigned in_width = OUT_WIDTH_10;
    static const unsigned n_filt = N_FILT_12;
    static const unsigned stride_height = 2;
    static const unsigned stride_width = 2;
    static const unsigned pool_height = 2;
    static const unsigned pool_width = 2;
    static const unsigned out_height = OUT_HEIGHT_12;
    static const unsigned out_width = OUT_WIDTH_12;
    static const unsigned pad_top = 0;
    static const unsigned pad_bottom = 0;
    static const unsigned pad_left = 0;
    static const unsigned pad_right = 0;
    static const nnet::Pool_Op pool_op = nnet::Max;
    static const unsigned reuse = 1;
};

struct config13 : nnet::dense_config {
    static const unsigned n_in = OUT_HEIGHT_12*OUT_WIDTH_12*N_FILT_12;
    static const unsigned n_out = N_LAYER_13;
    static const unsigned io_type = nnet::io_parallel;
    static const unsigned reuse_factor = 1;
    static const unsigned n_zeros = 0;
    static const unsigned n_nonzeros = 65536;
    static const bool store_weights_in_bram = false;
    typedef ap_fixed<16,6> accum_t;
    typedef model_default_t bias_t;
    typedef model_default_t weight_t;
    typedef ap_uint<1> index_t;
};

struct relu_config14 : nnet::activ_config {
    static const unsigned n_in = N_LAYER_13;
    static const unsigned table_size = 1024;
    static const unsigned io_type = nnet::io_parallel;
    static const unsigned reuse_factor = 1;
    typedef ap_fixed<18,8> table_t;
};

struct config15 : nnet::dense_config {
    static const unsigned n_in = N_LAYER_13;
    static const unsigned n_out = N_LAYER_15;
    static const unsigned io_type = nnet::io_parallel;
    static const unsigned reuse_factor = 1;
    static const unsigned n_zeros = 0;
    static const unsigned n_nonzeros = 2304;
    static const bool store_weights_in_bram = false;
    typedef ap_fixed<16,6> accum_t;
    typedef model_default_t bias_t;
    typedef model_default_t weight_t;
    typedef ap_uint<1> index_t;
};

struct softmax_config17 : nnet::activ_config {
    static const unsigned n_in = N_LAYER_15;
    static const unsigned table_size = 1024;
    static const unsigned io_type = nnet::io_parallel;
    static const unsigned reuse_factor = 1;
    static const nnet::softmax_implementation implementation = nnet::softmax_implementation::latency;
    typedef ap_fixed<18,8> exp_table_t;
    typedef ap_fixed<18,8> inv_table_t;
};


#endif
