'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Marcel Sawrin + Marcus Rueb
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

from src.gui_layout.ui_automl_settings import *


def automl_settings(self):
    """Activates the GUI window to pass the settings for
    AutoKeras training.

    You have to pass the settings according to the task of your
    AutoKeras model.
    """
    self.automl_settings_ui = UIAutoMLSettings(
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self.task,
        self)

    self.automl_settings_ui.epochs_factor.setText(str(self.max_epochs))
    self.automl_settings_ui.max_trials_factor.setText(str(self.max_trials))
    self.automl_settings_ui.max_size_factor.setText(str(self.max_size))
    self.automl_settings_ui.num_channels.setText(str(self.num_channels))
    self.automl_settings_ui.img_height.setText(str(self.img_height))
    self.automl_settings_ui.img_width.setText(str(self.img_width))

    self.automl_settings_ui.back.clicked.connect(
        lambda: next_window(self, "Back"))
    self.automl_settings_ui.next.clicked.connect(
        lambda: next_window(self, "Next"))

    self.setCentralWidget(self.automl_settings_ui)
    self.show()


def next_window(self, n):
    """
    Defines which one is the next window to open.

    Args:
        n:  Go forward or go back
    """

    if n == "Back":
        self.automl_task()

    elif n == "Next":
        try:
            self.max_epochs = int(
                self.automl_settings_ui.epochs_factor.text())
            self.max_trials = int(
                self.automl_settings_ui.max_trials_factor.text())
            self.max_size = int(
                self.automl_settings_ui.max_size_factor.text())
            self.num_channels = int(
                self.automl_settings_ui.num_channels.text())
            self.img_height = int(
                self.automl_settings_ui.img_height.text())
            self.img_width = int(
                self.automl_settings_ui.img_width.text())
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("Please enter a valid number for all parameters.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return

        reply = QMessageBox.question(
            self, 'Start training', 'Do you want to start model training now?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.automl_training()
        else:
            return
