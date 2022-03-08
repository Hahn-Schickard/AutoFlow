'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Marcel Sawrin + Marcus Rueb
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

from src.gui_layout.ui_automl_task import *


def automl_task(self):
    """Select a button to choose your device.

    You can choose via three different buttons on which device you want
    to exectue the model. If "Back" is pressed you get back to the start
    window. If you choose a device you get to the optimization window.
    """
    self.automl_task_ui = UIAutoMLTask(self.WINDOW_WIDTH, self.WINDOW_HEIGHT,
                                       self.FONT_STYLE, self)

    self.automl_task_ui.image_classification.clicked.connect(
        lambda: next_window(self, "Next", "imageClassification"))
    self.automl_task_ui.image_regression.clicked.connect(
        lambda: next_window(self, "Next", "imageRegression"))
    self.automl_task_ui.data_classification.clicked.connect(
        lambda: next_window(self, "Next", "dataClassification"))
    self.automl_task_ui.data_regression.clicked.connect(
        lambda: next_window(self, "Next", "dataRegression"))

    self.automl_task_ui.back.clicked.connect(
        lambda: next_window(self, "Back", None))

    self.setCentralWidget(self.automl_task_ui)
    self.show()


def next_window(self, n, task):
    """
    Defines which one is the next window to open.

    Args:
        n:      Go forward or go back
        task:   Model type to interpret the data
    """
    if n == "Back":
        self.automl_data()

    elif n == "Next":
        self.task = task
        print("Task:", self.task)

        if (self.task == "dataClassification" and
                os.path.isdir(self.data_loader_path) or
                self.task == "dataRegression" and
                os.path.isdir(self.data_loader_path)):

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("If you want to use this task please use a file "
                        "as dataloader.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return

        self.automl_settings()
