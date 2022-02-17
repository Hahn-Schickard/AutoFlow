''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import os
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def start_autokeras(self):
    """Start the AutoKeras training

    Depending on the task selected, the training of
    a neural network is started using AutoKeras.
    """
    if self.task == "imageClassification":
        os.system(
            f"""start /B start cmd.exe @cmd /k python src/AutoML/ImageClassifier.py --project_name={self.project_name} 
            --output_path={self.output_path} --data_path={self.data_loader_path} --max_trials={self.max_trials} 
            --max_epochs={self.max_epochs} --max_size={self.max_size} --num_channels={self.num_channels} 
            --img_height={self.img_height} --img_width={self.img_width}"""
        )

    if self.task == "imageRegression":
        os.system(
            f"""start /B start cmd.exe @cmd /k python src/AutoML/ImageRegressor.py --project_name={self.project_name} 
            --output_path={self.output_path} --data_path={self.data_loader_path} --ParamConstraint={self.params_check} 
            --ParamFactor={self.params_factor} --FlopConstraint={self.floats_check} --FlopFactor={self.floats_factor} 
            --ComplexConstraint={self.complex_check} --ComplexFactor={self.complex_factor} --max_size={self.max_size} 
            --max_trials={self.max_trials} --max_epochs={self.max_epochs}"""
        )