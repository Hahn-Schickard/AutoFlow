'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: GPL-3.0
============================================================================'''

from src.gui_layout.ui_create_project import *


def create_project(self):
    """Activates the GUI window to create the project.

    When the load button is selected, the optimization algorithms
    are applied if any are selected. Also, the model is converted
    and the files are created.
    """
    self.create_project_ui = UICreateProject(
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE,
        self.model_path, self.project_name, self.output_path,
        self.data_loader_path, self.optimizations, self.prun_type,
        self.prun_factor_dense, self.prun_factor_conv, self.prun_acc_type,
        self.prun_acc, self.quant_dtype, self.separator, self.decimal,
        self.csv_target_label, self.target, self)

    if isinstance(self.model_memory, int):
        self.create_project_ui.model_memory.setText(str(self.model_memory))

    set_window_labels(self, self.create_project_ui)

    self.create_project_ui.back.clicked.connect(
        lambda: next_window(self, "Back", self.optimizations,
                            self.create_project_ui))

    self.create_project_ui.load.clicked.connect(
        lambda: next_window(self, "Next", self.optimizations,
                            self.create_project_ui))

    self.create_project_ui.prune_model.request_signal.connect(
        lambda: self.convert_create(self.create_project_ui))
    self.create_project_ui.conv_build_load.request_signal.connect(
        lambda: self.terminate_thread(self.create_project_ui))

    self.create_project_ui.finish.clicked.connect(self.close)

    self.setCentralWidget(self.create_project_ui)
    self.show()


def set_window_labels(self, cur_window):
    """
    Set and align the labels of the load window.

    Args:
        cur_window:      GUI window from which the function is executed
    """
    self.set_label(cur_window.project_name_label_2, self.project_name,
                   Qt.AlignLeft)
    self.set_label(cur_window.output_path_label_2, self.output_path,
                   Qt.AlignLeft)
    self.set_label(cur_window.model_path_label_2, self.model_path,
                   Qt.AlignLeft)
    self.set_label(cur_window.target_label_2, self.target, Qt.AlignLeft)
    if ("Pruning" in self.optimizations and
            "Quantization" in self.optimizations):
        self.set_label(cur_window.optimizations_label_2,
                       "Pruning + Quantization", Qt.AlignLeft)
    elif len(self.optimizations) != 0:
        self.set_label(cur_window.optimizations_label_2, self.optimizations[0],
                       Qt.AlignLeft)
    else:
        self.set_label(cur_window.optimizations_label_2, "-", Qt.AlignLeft)
    if "Pruning" in self.optimizations:
        if "Factor" in self.prun_type:
            self.set_label(
                cur_window.pruning_label_2, "Pruningfactor dense: " +
                str(self.prun_factor_dense) + "%," +
                "   Pruningfactor conv: " + str(self.prun_factor_conv) +
                "%", Qt.AlignLeft)
        else:
            if "Minimal accuracy" in self.prun_acc_type:
                self.set_label(
                    cur_window.pruning_label_2, "Minimal accuracy to reach: " +
                    str(self.prun_acc) + "%", Qt.AlignLeft)
            else:
                self.set_label(
                    cur_window.pruning_label_2, "Maximal accuracy loss: " +
                    str(self.prun_acc) + "%", Qt.AlignLeft)
    if "Quantization" in self.optimizations:
        if "int8 only" in self.quant_dtype:
            self.set_label(cur_window.quantization_label_2, "Int8 only",
                           Qt.AlignLeft)
        else:
            self.set_label(cur_window.quantization_label_2,
                           "Int8 with float32 fallback", Qt.AlignLeft)
    self.set_label(cur_window.data_loader_label_2, self.data_loader_path,
                   Qt.AlignLeft)


def next_window(self, n, optimizations, cur_window):
    """
    Defines which one is the next window to open if you
    press "Back". If optimization algorithms were previously
    selected, the data loader is the next window otherwise
    the optimization window.

    Args:
        n:              Go forward or go back
        optimizations:  Selected optimization algorithms
        cur_window:      GUI window from which the function is executed
    """
    if n == "Back":
        try:
            self.model_memory = int(cur_window.model_memory.text())
        except:
            self.model_memory = None

        if optimizations:
            self.dataloader()
        else:
            self.optimization_algo()

    elif n == "Next":
        if "MCU" in self.target:
            try:
                if (int(cur_window.model_memory.text()) < 5 or
                        int(cur_window.model_memory.text()) > 1000):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)

                    msg.setText("Please enter a number for model memory"
                                "between 5 and 1000 kB.")
                    msg.setWindowTitle("Warning")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec_()
                    return
                else:
                    self.model_memory = int(cur_window.model_memory.text())
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)

                msg.setText("Please enter a valid number for model memory.")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
                return

        reply = QMessageBox.question(
            self, 'Create Project', 'Do you want to create the project now?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.model_pruning(cur_window)
        else:
            return
