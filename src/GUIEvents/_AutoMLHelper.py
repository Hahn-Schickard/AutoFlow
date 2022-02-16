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
            f"start /B start cmd.exe @cmd /k python src/AutoML/ImageClassifier.py --ProjectName={self.project_name} --OutputPath={self.output_path} --DataPath={self.data_loader_path} --MaxTrials={self.max_trials} --MaxEpochs={self.max_epochs} --MaxSize={self.max_size} --NumChannels={self.num_channels} --ImgHeight={self.img_height} --ImgWidth={self.img_width}"
        )

    if self.task == "imageRegression":
        os.system(
            f"start /B start cmd.exe @cmd /k python src/AutoML/ImageRegressor.py --ProjectName={self.project_name} --OutputPath={self.output_path} --DataPath={self.data_loader_path} --ParamConstraint={self.params_check} --ParamFactor={self.params_factor} --FlopConstraint={self.floats_check} --FlopFactor={self.floats_factor} --ComplexConstraint={self.complex_check} --ComplexFactor={self.complex_factor} --MaxSize={self.max_size} --MaxTrials={self.max_trials} --MaxEpochs={self.max_epochs}"
        )