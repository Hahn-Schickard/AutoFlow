'''Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

import sys
sys.path.append("..")   # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.AutoML.ImageClassifier import image_classifier
from src.AutoML.ImageRegressor import image_regressor
from src.AutoML.DataClassifier import data_classifier
from src.AutoML.DataRegressor import data_regressor


class Autokeras(QThread):
    """Thread to train models using AutoKeras.

    Attributes:
        project_name:   Name of the project to be created
        output_path:    Output path of the project to be created
        data_path:      Path of the folder or file with the training data
        max_trials:     The maximum number of attempts for AutoKeras to find
                        the best model
        max_epochs:     Number of maximal training epochs
        max_size:       The maximum model size that AutoKeras is allowed to
                        use.
        num_channels:   Number of channels of the inputdata for images
        img_height:     Height of the input images
        img_width:      Width of the input images
    """
    request_signal = pyqtSignal()

    def __init__(self, project_name, output_path, data_path, task, max_trials,
                 max_epochs, max_size, num_channels, img_height, img_width,
                 separator, decimal, csv_target_label):
        QThread.__init__(self)
        self.project_name = project_name
        self.output_path = output_path
        self.data_path = data_path
        self.task = task
        self.max_trials = max_trials
        self.max_epochs = max_epochs
        self.max_size = max_size
        self.num_channels = num_channels
        self.img_height = img_height
        self.img_width = img_width
        self.separator = separator
        self.decimal = decimal
        self.csv_target_label = csv_target_label

    def run(self):
        """Activates the thread

        Depending on the task selected, the training of
        a neural network is started using AutoKeras.
        """
        if self.task == "imageClassification":
            image_classifier(
                self.project_name, self.output_path, self.data_path,
                max_trials=self.max_trials, max_epochs=self.max_epochs,
                max_size=self.max_size, num_channels=self.num_channels,
                img_height=self.img_height, img_width=self.img_width,
                separator=self.separator, decimal=self.decimal,
                csv_target_label=self.csv_target_label)
        elif self.task == "imageRegression":
            image_regressor(
                self.project_name, self.output_path, self.data_path,
                max_trials=self.max_trials, max_epochs=self.max_epochs,
                max_size=self.max_size, num_channels=self.num_channels,
                img_height=self.img_height, img_width=self.img_width,
                separator=self.separator, decimal=self.decimal,
                csv_target_label=self.csv_target_label)
        elif self.task == "dataClassification":
            data_classifier(
                self.project_name, self.output_path, self.data_path,
                max_trials=self.max_trials, max_epochs=self.max_epochs,
                max_size=self.max_size, separator=self.separator,
                decimal=self.decimal, csv_target_label=self.csv_target_label)
        elif self.task == "dataRegression":
            data_regressor(
                self.project_name, self.output_path, self.data_path,
                max_trials=self.max_trials, max_epochs=self.max_epochs,
                max_size=self.max_size, separator=self.separator,
                decimal=self.decimal, csv_target_label=self.csv_target_label)

        self.request_signal.emit()

    def stop_thread(self):
        """Ends the thread
        """
        self.terminate()
