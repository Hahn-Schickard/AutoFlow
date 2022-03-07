'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Marcel Sawrin + Marcus Rueb
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

from src.gui_layout.ui_automl_data import *


def automl_data(self):
    """Activates the GUI window to select output path, project name
       and data path to train the AutoKeras model.

    If the variables "project_name", "output_path" and "data_path" contain
    strings these are set. This data can be entered/selected via an input
    field and browse window. If you select the "Back" button you get to the
    start window of the GUI. If "Next" is pressed it is checked if the
    before mentioned variables are not empty. When at least one of them
    is empty you get an error message. Otherwise you get to the task window.
    """
    self.automl_data_ui = UIAutoMLData(self.WINDOW_WIDTH, self.WINDOW_HEIGHT,
                                       self.FONT_STYLE, self)

    if self.output_path is not None:
        self.automl_data_ui.output_path_label.setText(self.output_path)

    if self.project_name is not None:
        self.automl_data_ui.project_name.setText(self.project_name)

    if self.data_loader_path is not None:
        self.automl_data_ui.data_path_label.setText(self.data_loader_path)

    self.automl_data_ui.output_path_browse.clicked.connect(
        lambda: self.get_output_path(self.automl_data_ui.output_path_label))
    self.automl_data_ui.select_data_browse.clicked.connect(
        lambda: self.get_data_loader(self.automl_data_ui,
                                     self.automl_data_ui.data_path_label))
    self.automl_data_ui.next.clicked.connect(
        lambda: next_window(self, "Next"))
    self.automl_data_ui.back.clicked.connect(
        lambda: next_window(self, "Back"))

    self.setCentralWidget(self.automl_data_ui)
    self.show()


def next_window(self, n):
    """
    Defines which one is the next window to open.

    Args:
        n:  Go forward or go back
    """
    self.project_name = self.automl_data_ui.project_name.text()
    self.output_path_label = self.automl_data_ui.output_path_label.text()
    self.data_loader_path = self.automl_data_ui.data_path_label.text()

    if n == "Back":
        self.gui_start()

    elif n == "Next":
        if (self.project_name == "" or self.output_path_label == "" or
                self.data_loader_path == ""):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("Please enter your data")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return

        print("Project name:", self.project_name)
        print("Output path:", self.output_path_label)
        print("Data path:", self.data_loader_path)
        self.automl_task()
