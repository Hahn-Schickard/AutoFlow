'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Marcel Sawrin + Marcus Rueb
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

from src.gui_layout.ui_automl_training import *


def automl_training(self):
    """AutoKeras training process get started.

    The process of training models accoring the passed settings
    get started. You have to wait until the process is finished.
    After this you get back to the start window.
    """
    self.automl_training_ui = UIAutoMLTraining(
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE,
        self.project_name, self.output_path, self.data_loader_path,
        self.task, self.max_trials, self.max_epochs, self.max_size,
        self.num_channels, self.img_height, self.img_width, self.separator,
        self.decimal, self.csv_target_label, self)

    self.automl_training_ui.loading_images.start()
    self.automl_training_ui.autokeras.start()

    self.automl_training_ui.autokeras.request_signal.connect(
        lambda: next_window(self))
    print("AutoKeras finished")

    self.setCentralWidget(self.automl_training_ui)
    self.show()


def next_window(self):
    """
    After AutoKeras training is finished, stop the
    the two threads and return to the start window
    of the GUI.
    """
    self.automl_training_ui.autokeras.stop_thread()
    self.automl_training_ui.loading_images.stop_thread()
    self.gui_start()
