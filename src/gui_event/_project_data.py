'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.gui_layout.ui_project_data import *


def project_data(self):
    """Activates the GUI window to select output path, project name
       and model path.

    If the variables "project_name", "output_path" and "model_path" contain
    strings these are set. This data can be entered/selected via an input
    field and browse window. If you select the "Back" button you get to the
    start window of the GUI. If "Next" is pressed it is checked if the
    before mentioned variables are not empty. When at least one of them
    is empty you get an error message. Otherwise you get to the target window.
    """
    self.project_data_ui = UIProjectData(self.WINDOW_WIDTH, self.WINDOW_HEIGHT,
                                         self.FONT_STYLE, self)

    self.project_data_ui.project_name.setText(self.project_name)
    self.set_label(self.project_data_ui.output_path_label, self.output_path,
                   Qt.AlignCenter)
    self.set_label(self.project_data_ui.model_path_label, self.model_path,
                   Qt.AlignCenter)

    self.project_data_ui.output_path_Browse.clicked.connect(
        lambda: self.get_output_path(self.project_data_ui.output_path_label))
    self.project_data_ui.select_model_browse.clicked.connect(
        lambda: self.get_model_path(self.project_data_ui.model_path_label))

    self.project_data_ui.next.clicked.connect(
        lambda: next_window(self, "Next"))
    self.project_data_ui.back.clicked.connect(
        lambda: next_window(self, "Back"))

    self.setCentralWidget(self.project_data_ui)
    self.show()


def next_window(self, n):
    """
    Defines which one is the next window to open.

    Args:
        n:  Go forward or go back
    """
    self.project_name = self.project_data_ui.project_name.text()
    self.output_path = self.project_data_ui.output_path_label.text()
    self.model_path = self.project_data_ui.model_path_label.text()

    if n == "Back":
        self.gui_start()

    elif n == "Next":
        if (self.project_name == "" or self.model_path == "" or
                self.output_path == ""):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("Please enter your data")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()

            return

        print("Project name:", self.project_name)
        print("Output path:", self.output_path)
        print("Model path:", self.model_path)
        self.target_platform()
