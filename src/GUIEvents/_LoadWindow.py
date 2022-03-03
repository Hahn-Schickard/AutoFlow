''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

from src.GUILayout.UILoadWindow import *


def LoadWindow(self):
    """Activates the GUI window to create the project.

    When the load button is selected, the optimization algorithms
    are applied if any are selected. Also, the model is converted
    and the files are created.
    """
    self.Window5 = UILoadWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self.model_path,
                            self.project_name, self.output_path, self.data_loader_path, self.optimizations,
                            self.prun_type, self.prun_factor_dense, self.prun_factor_conv, self.prun_acc_type,
                            self.prun_acc, self.quant_dtype, self.separator, self.decimal, self.csv_target_label,
                            self.target, self)
    
    if isinstance(self.model_memory, int):
        self.Window5.model_memory.setText(str(self.model_memory))
    
    setWindowLabels(self, self.Window5)
    
    
    self.Window5.back.clicked.connect(lambda:nextWindow(self, "Back", self.optimizations, self.Window5))
    
    self.Window5.load.clicked.connect(lambda:nextWindow(self, "Next", self.optimizations, self.Window5))
    
    self.Window5.prune_model.request_signal.connect(lambda:self.convert_create(self.Window5))
    self.Window5.conv_build_load.request_signal.connect(lambda:self.terminate_thread(self.Window5))
    
    self.Window5.finish.clicked.connect(self.close)
    
    self.setCentralWidget(self.Window5)
    self.show()


def setWindowLabels(self, CurWindow):
    """
    Set and align the labels of the load window.

    Args:
        CurWindow:      GUI window from which the function is executed
    """
    self.set_label(CurWindow.project_name_label_2, self.project_name, Qt.AlignLeft)
    self.set_label(CurWindow.output_path_label_2, self.output_path, Qt.AlignLeft)
    self.set_label(CurWindow.model_path_label_2, self.model_path, Qt.AlignLeft)
    self.set_label(CurWindow.target_label_2, self.target, Qt.AlignLeft)
    if "Pruning" in self.optimizations and "Quantization" in self.optimizations:
        self.set_label(CurWindow.optimizations_label_2, "Pruning + Quantization", Qt.AlignLeft)
    elif len(self.optimizations) != 0:
        self.set_label(CurWindow.optimizations_label_2, self.optimizations[0], Qt.AlignLeft)
    else:
        self.set_label(CurWindow.optimizations_label_2, "-", Qt.AlignLeft)
    if "Factor" in self.prun_type:
        self.set_label(CurWindow.pruning_label_2, "Pruningfactor dense: " + 
                str(self.prun_factor_dense) + "%," + "   Pruningfactor conv: " + 
                str(self.prun_factor_conv) + "%", Qt.AlignLeft)
    else:
        if "Minimal accuracy" in self.prun_acc_type:
            self.set_label(CurWindow.pruning_label_2, "Minimal accuracy to reach: " + 
                    str(self.prun_acc) + "%", Qt.AlignLeft)
        else:
            self.set_label(CurWindow.pruning_label_2, "Maximal accuracy loss: " + 
                    str(self.prun_acc) + "%", Qt.AlignLeft)
    if "int8 only" in self.quant_dtype:
        self.set_label(CurWindow.quantization_label_2, "Int8 only", Qt.AlignLeft)
    else:
        self.set_label(CurWindow.quantization_label_2, "Int8 with float32 fallback", Qt.AlignLeft)
    self.set_label(CurWindow.data_loader_label_2, self.data_loader_path, Qt.AlignLeft)


def nextWindow(self, n, optimizations, CurWindow):
    """
    Defines which one is the next window to open if you
    press "Back". If optimization algorithms were previously
    selected, the data loader is the next window otherwise
    the optimization window.

    Args:
        n:              Go forward or go back
        optimizations:  Selected optimization algorithms
        CurWindow:      GUI window from which the function is executed
    """
    if n == "Back":
        try:
            self.model_memory = int(CurWindow.model_memory.text())
        except:
            self.model_memory = None

        if optimizations:
            self.DataloaderWindow()
        else:
            self.OptiWindow()
    
    elif n == "Next":
        if "MCU" in self.target:
            try:
                if int(CurWindow.model_memory.text()) < 5 or int(CurWindow.model_memory.text()) > 1000:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                        
                    msg.setText("Please enter a number for model memory between 5 and 1000 kB.")
                    msg.setWindowTitle("Warning")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec_()
                    return
                else:
                    self.model_memory = int(CurWindow.model_memory.text())
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                    
                msg.setText("Please enter a valid number for model memory.")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
                return

        reply = QMessageBox.question(self, 'Create Project', 'Do you want to create the project now?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.model_pruning(CurWindow)
        else:
            return