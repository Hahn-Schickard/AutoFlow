''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

"""This is a splittet method from the Mainwindow class which contain the logic for the AutoMLData window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""

import os
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def start_autokeras(self):
    if "Params" in self.constraints:
        self.params_check = True

    if "Floats" in self.constraints:
        self.floats_check = True

    if "Complex" in self.constraints:
        self.complex_check = True

    if self.task == "imageClassification":
        # print("self.project_name:",self.project_name)
        # print("self.output_path:",self.output_path)
        # print("self.data_loader_path:",self.data_loader_path)
        # print("self.params_check:",self.params_check)
        # print("self.params_factor:",self.params_factor)
        # print("self.floats_check:",self.floats_check)
        # print("self.floats_factor:",self.floats_factor)
        # print("self.complex_check:", self.complex_check)
        # print("self.complex_factor:",self.complex_factor)
        # print("self.max_size:",self.max_size)
        # print("self.max_trials:",self.max_trials)
        # print("self.max_epoch:",self.max_epoch)
        os.system(
            f"start /B start cmd.exe @cmd /k python src/AutoML/ImageClassifier.py --ProjectName={self.project_name} --OutputPath={self.output_path_ml} --DataPath={self.data_loader_path_ml} --ParamConstraint={self.params_check} --ParamFactor={self.params_factor} --FlopConstraint={self.floats_check} --FlopFactor={self.floats_factor} --ComplexConstraint={self.complex_check} --ComplexFactor={self.complex_factor} --MaxSize={self.max_size} --MaxTrials={self.max_trials} --MaxEpochs={self.max_epoch}"
        )

    if self.task == "imageRegression":
        os.system(
            f"start /B start cmd.exe @cmd /k python src/AutoML/ImageRegressor.py --ProjectName={self.project_name} --OutputPath={self.output_path_ml} --DataPath={self.data_loader_path_ml} --ParamConstraint={self.params_check} --ParamFactor={self.params_factor} --FlopConstraint={self.floats_check} --FlopFactor={self.floats_factor} --ComplexConstraint={self.complex_check} --ComplexFactor={self.complex_factor} --MaxSize={self.max_size} --MaxTrials={self.max_trials} --MaxEpochs={self.max_epoch}"
        )


# def get_output_path_ml(self, CurWindow):
#     self.output_path_ml = QFileDialog.getExistingDirectory(
#         self, "Select the output path", "./"
#     )
#     CurWindow.Output_Pfad.setText(self.output_path_ml)
#     print(CurWindow.Output_Pfad.text())


# def get_data_loader_path_ml(self, CurWindow):
#     self.data_loader_path_ml = QFileDialog.getExistingDirectory(#getOpenFileName(
#         self, "Select your data loader script", "./"
#     )#[0]
#     CurWindow.Daten_Pfad.setText(self.data_loader_path_ml)
#     print(CurWindow.Daten_Pfad.text())