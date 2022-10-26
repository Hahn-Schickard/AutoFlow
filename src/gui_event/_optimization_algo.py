'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: GPL-3.0
============================================================================'''

from src.gui_layout.ui_optimization_algo import *


def optimization_algo(self):
    """Activates the GUI window to select the optimizations.

    Via the two buttons Pruning and Quantization, the optimization
    algorithms can be selected, if desired. The pruning factors can
    be entered via input fields and the data types for the quantization
    via buttons. If "Next" is pressed and pruning and/or quantization
    have been selected as optimization algorithms, it is checked whether
    the entries are correct and complete.
    """

    self.optimization_algo_ui = UIOptimization(
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self.target,
        self)

    if "Pruning" in self.optimizations:
        self.optimization_algo_ui.pruning.setChecked(True)
        self.set_pruning(self.optimization_algo_ui)
    if "Quantization" in self.optimizations:
        self.optimization_algo_ui.quantization.setChecked(True)
        self.set_quantization(self.optimization_algo_ui)
        if self.quant_dtype is not None:
            if "int8 with float fallback" in self.quant_dtype:
                self.optimization_algo_ui.quant_int_only.setChecked(False)
                self.optimization_algo_ui.quant_int.setChecked(True)
            elif "int8 only" in self.quant_dtype:
                self.optimization_algo_ui.quant_int_only.setChecked(True)
                self.optimization_algo_ui.quant_int.setChecked(False)
    self.optimization_algo_ui.pruning.toggled.connect(
        lambda: self.set_pruning(self.optimization_algo_ui))
    self.optimization_algo_ui.quantization.toggled.connect(
        lambda: self.set_quantization(self.optimization_algo_ui))

    self.optimization_algo_ui.prun_fac.clicked.connect(
        lambda: self.set_prun_type("Factor", self.optimization_algo_ui, False))
    self.optimization_algo_ui.prun_acc.clicked.connect(
        lambda: self.set_prun_type("Accuracy", self.optimization_algo_ui,
                                   False))

    self.optimization_algo_ui.min_acc.clicked.connect(
        lambda: self.set_prun_acc_type("Minimal accuracy",
                                       self.optimization_algo_ui))
    self.optimization_algo_ui.acc_loss.clicked.connect(
        lambda: self.set_prun_acc_type("Accuracy loss",
                                       self.optimization_algo_ui))

    self.optimization_algo_ui.quant_int.clicked.connect(
        lambda: self.set_quant_dtype("int8 with float fallback",
                                     self.optimization_algo_ui))
    self.optimization_algo_ui.quant_int_only.clicked.connect(
        lambda: self.set_quant_dtype("int8 only", self.optimization_algo_ui))

    self.optimization_algo_ui.back.clicked.connect(
        lambda: next_window(self, "Back"))
    self.optimization_algo_ui.next.clicked.connect(
        lambda: next_window(self, "Next"))

    self.setCentralWidget(self.optimization_algo_ui)
    self.show()


def next_window(self, n):
    """
    Defines which one is the next window to open.

    Args:
        n:  Go forward or go back
    """
    if n == "Back":
        if "Pruning" in self.optimizations:
            try:
                if "Factor" in self.prun_type:
                    self.prun_factor_dense = (int(
                        self.optimization_algo_ui.pruning_dense.text()))
                    self.prun_factor_conv = (int(
                        self.optimization_algo_ui.pruning_conv.text()))
                elif "Accuracy" in self.prun_type:
                    self.prun_acc = int(
                        self.optimization_algo_ui.prun_acc_edit.text())
            except:
                self.prun_acc = None
                self.prun_factor_dense = None
                self.prun_factor_conv = None

        self.target_platform()

    elif n == "Next":
        if "Pruning" in self.optimizations:
            if self.prun_type is None:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)

                msg.setText("Select a pruning type")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
                return

            elif "Factor" in self.prun_type:
                try:
                    if (int(self.optimization_algo_ui.pruning_dense.text()) >
                        95 or
                        int(self.optimization_algo_ui.pruning_conv.text()) >
                            95):
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)

                        msg.setText("Enter pruning factors of up to 95%")
                        msg.setWindowTitle("Warning")
                        msg.setStandardButtons(
                            QMessageBox.Ok | QMessageBox.Cancel)
                        msg.exec_()
                        return

                    self.prun_factor_dense = (int(
                        self.optimization_algo_ui.pruning_dense.text()))
                    self.prun_factor_conv = (int(
                        self.optimization_algo_ui.pruning_conv.text()))
                except:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)

                    msg.setText("Please enter a number for pruning or "
                                "disable it.")
                    msg.setWindowTitle("Warning")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec_()
                    return

            elif "Accuracy" in self.prun_type:
                try:
                    if self.prun_acc_type is None:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)

                        msg.setText("Select a type for pruning")
                        msg.setWindowTitle("Warning")
                        msg.setStandardButtons(
                            QMessageBox.Ok | QMessageBox.Cancel)
                        msg.exec_()
                        return

                    if "Minimal accuracy" in self.prun_acc_type:
                        if (int(
                            self.optimization_algo_ui.prun_acc_edit.text()) <=
                            50 or
                            int(
                            self.optimization_algo_ui.prun_acc_edit.text()) >
                                99):
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)

                            msg.setText("Enter a value for minimal Accuracy "
                                        "which is higher than 50% and lower "
                                        "99%")
                            msg.setWindowTitle("Warning")
                            msg.setStandardButtons(
                                QMessageBox.Ok | QMessageBox.Cancel)
                            msg.exec_()
                            return
                    else:
                        if (int(
                            self.optimization_algo_ui.prun_acc_edit.text()) <
                            1 or
                            int(
                            self.optimization_algo_ui.prun_acc_edit.text()) >
                                20):
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)

                            msg.setText("Enter a value for maximal accuracy "
                                        "loss between 1% and 20%")
                            msg.setWindowTitle("Warning")
                            msg.setStandardButtons(
                                QMessageBox.Ok | QMessageBox.Cancel)
                            msg.exec_()
                            return

                    self.prun_acc = int(
                        self.optimization_algo_ui.prun_acc_edit.text())
                except:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)

                    msg.setText("Please enter a number for pruning or "
                                "disable it.")
                    msg.setWindowTitle("Warning")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec_()
                    return

        if "Quantization" in self.optimizations and self.quant_dtype is None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("Enter a dtype for quantization.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return

        if not self.optimizations or "int8 with float fallback" in self.quant_dtype:
            print("No optimization")
            self.create_project()
        else:
            print("Optimizations:", self.optimizations)
            if "Pruning" in self.optimizations:
                print("Pruning type:", self.prun_type)
                if "Factor" in self.prun_type:
                    print("Pruning factor dense:", self.prun_factor_dense)
                    print("Pruning factor conv:", self.prun_factor_conv)
                else:
                    if "Minimal accuracy" in self.prun_acc_type:
                        print("Minimal accuracy to reach:", self.prun_acc)
                    else:
                        print("Maximal accuracy loss:", self.prun_acc)
            if "Quantization" in self.optimizations:
                print("Quantization type:", self.quant_dtype)
            self.dataloader()
