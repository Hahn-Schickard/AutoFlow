'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

import sys
sys.path.append("..")   # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.converter.create_project import convert_and_write


class ConvertBuild(QThread):
    """Thread to convert the model and build the project.

    Attributes:
        model_path:         Path of the model to convert
        project_name:       Name of the project to be created
        output_path:        Output path of the project to be created
        optimizations:      Selected optimization algorithms
        data_loader_path:   Path of the folder or file with the training data
        quant_dtype:        Data type to quantize to
        separator:          Separator for reading a CSV file
        decimal:            Decimal for reading a CSV file
        csv_target_label:   Target label from the CSV file
        model_memory:       Memory to allocate for the model on MCUs
        target:             Target to execute the neural network
    """

    request_signal = pyqtSignal()

    def __init__(self, model_path, project_name, output_path, optimizations,
                 data_loader_path, quant_dtype, separator, decimal,
                 csv_target_label, target):
        QThread.__init__(self)
        self.model_path = model_path
        self.project_name = project_name
        self.output_path = output_path
        self.optimizations = optimizations
        self.data_loader_path = data_loader_path
        self.quant_dtype = quant_dtype
        self.separator = separator
        self.decimal = decimal
        self.csv_target_label = csv_target_label
        self.model_memory = None
        self.target = target

    def set_model_memory(self, model_memory):
        """Sets the model memory value

        Args:
            model_memory:   Memory to allocate for the model on MCUs
        """
        self.model_memory = model_memory

    def run(self):
        """Activates the thread

        Calls the function to convert the model and build the project.
        When the function is finished, a signal is emitted.
        """
        print("ConvertBuild thread started")
        convert_and_write(
            self.model_path, self.project_name, self.output_path,
            self.optimizations, self.data_loader_path, self.quant_dtype,
            self.separator, self.decimal, self.csv_target_label,
            self.model_memory, self.target)
        self.request_signal.emit()

    def stop_thread(self):
        """Ends the thread
        """
        self.terminate()
