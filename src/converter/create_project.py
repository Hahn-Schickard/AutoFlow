'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: GPL-3.0
============================================================================'''

import os
import ntpath

from src.converter.convert_keras_to_cc import *
from src.converter.write_files_uc import *


def convert_and_write(keras_model_dir, project_name, output_path,
                      optimizations, data_loader_path, quant_dtype,
                      separator, decimal, csv_target_label, model_memory,
                      target):
    """
    A keras model get's converted into a C++ model, the project directory is
    created and all files that are needed to compile the project get generated.

    Args:
        keras_model_dir:  Path of the keras model
        project_name:     Name of the project which should be generated
        output_path:      Directory where the project should be generated
        optimization:     Selected optimization algorithms
        data_loader_path: Path of the folder or file with the training data
        quant_dtype:      Data type to quantize to
        separator:        Separator for reading a CSV file
        decimal:          Decimal for reading a CSV file
        csv_target_label: Target label from the CSV file
        model_memory:     Preallocate a certain amount of memory for input,
                          output, and intermediate arrays in kilobytes
        target:           Target to execute the neural network
    """
    print("convert_and_write function called")
    model_name = ntpath.basename(keras_model_dir)
    model_name, _ = os.path.splitext(model_name)
    model_input_neurons = 1

    project_dir = create_project_dir(project_name, output_path, target)

    model_input_shape, model_output_neurons = convert_model_to_tflite(
        keras_model_dir, project_dir, model_name, optimizations,
        data_loader_path, quant_dtype, separator, decimal, csv_target_label)

    if "MCU" in target:
        convert_model_to_cpp(model_name, project_dir)

        for i in range(1, len(model_input_shape)):
            model_input_neurons = model_input_neurons * model_input_shape[i]

        main_functions(project_dir, model_name, model_input_neurons,
                       model_output_neurons, quant_dtype, model_memory)
        tensorflow_library(project_dir)

    if 'Pruning' in optimizations:
        pruned_keras_model(keras_model_dir, project_dir, model_name)
        os.remove(keras_model_dir)
