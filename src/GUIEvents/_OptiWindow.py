''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

from src.GUILayout.UIOptiWindow import *
        

def OptiWindow(self):
    """Activates the GUI window to select the optimizations.

    Via the two buttons Pruning and Quantization, the optimization
    algorithms can be selected, if desired. The pruning factors can
    be entered via input fields and the data types for the quantization
    via buttons. If "Next" is pressed and pruning and/or quantization
    have been selected as optimization algorithms, it is checked whether
    the entries are correct and complete.
    """

    self.Window3 = UIOptiWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self.target, self)
    
    if "Pruning" in self.optimizations:
        self.Window3.pruning.setChecked(True)
        self.set_pruning(self.Window3)
        self.Window3.pruning_dense.setText(str(self.prun_factor_dense))
        self.Window3.pruning_conv.setText(str(self.prun_factor_conv))
    if "Quantization" in self.optimizations:
        self.Window3.quantization.setChecked(True)
        self.set_quantization(self.Window3)
        if self.quant_dtype != None:
            if "int8 with float fallback" in self.quant_dtype:
                self.Window3.quant_int_only.setChecked(False)  
                self.Window3.quant_int.setChecked(True)              
            elif "int8 only" in self.quant_dtype:
                self.Window3.quant_int_only.setChecked(True)  
                self.Window3.quant_int.setChecked(False)
    self.Window3.pruning.toggled.connect(lambda:self.set_pruning(self.Window3))
    self.Window3.quantization.toggled.connect(lambda:self.set_quantization(self.Window3))
    
    self.Window3.prun_fac.clicked.connect(lambda:self.set_prun_type("Factor", self.Window3, False))
    self.Window3.prun_acc.clicked.connect(lambda:self.set_prun_type("Accuracy", self.Window3, False))
    
    self.Window3.min_acc.clicked.connect(lambda:self.set_prun_acc_type("Minimal accuracy", self.Window3))
    self.Window3.acc_loss.clicked.connect(lambda:self.set_prun_acc_type("Accuracy loss", self.Window3))
    
    self.Window3.quant_int.clicked.connect(lambda:self.set_quant_dtype("int8 with float fallback", self.Window3))
    self.Window3.quant_int_only.clicked.connect(lambda:self.set_quant_dtype("int8 only", self.Window3))
    
    self.Window3.back.clicked.connect(lambda:nextWindow(self, "Back"))
    self.Window3.next.clicked.connect(lambda:nextWindow(self, "Next"))
    
    self.setCentralWidget(self.Window3)
    self.show()


def nextWindow(self,n):
    """
    Defines which one is the next window to open.

    Args:
        n:  Go forward or go back
    """
    if n == "Back":
        if "Pruning" in self.optimizations:
            try:
                if "Factor" in self.prun_type:
                    self.prun_factor_dense = int(self.Window3.pruning_dense.text())
                    self.prun_factor_conv = int(self.Window3.pruning_conv.text())
                elif "Accuracy" in self.prun_type:
                    self.prun_acc = int(self.Window3.prun_acc_edit.text())
            except:
                self.prun_acc = ""
                self.prun_factor_dense = ""
                self.prun_factor_conv = ""
        
        self.TargetWindow()
    
    elif n == "Next":
        if "Pruning" in self.optimizations:
            if self.prun_type == None:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                
                msg.setText("Select a pruning type")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
                return
            
            elif "Factor" in self.prun_type:
                try:
                    if int(self.Window3.pruning_dense.text()) > 95  or int(self.Window3.pruning_conv.text()) > 95:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        
                        msg.setText("Enter pruning factors of up to 95%")
                        msg.setWindowTitle("Warning")
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        msg.exec_()
                        return
                    
                    self.prun_factor_dense = int(self.Window3.pruning_dense.text())
                    self.prun_factor_conv = int(self.Window3.pruning_conv.text())
                except:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    
                    msg.setText("Please enter a number for pruning or disable it.")
                    msg.setWindowTitle("Warning")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec_()
                    return

            elif "Accuracy" in self.prun_type:
                try:
                    if self.prun_acc_type == None:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        
                        msg.setText("Select a type for pruning")
                        msg.setWindowTitle("Warning")
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        msg.exec_()
                        return

                    if "Minimal accuracy" in self.prun_acc_type:
                        if int(self.Window3.prun_acc_edit.text()) <= 50 or int(self.Window3.prun_acc_edit.text()) > 99:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            
                            msg.setText("Enter a value for minimal Accuracy which is higher than 50% and lower 99%")
                            msg.setWindowTitle("Warning")
                            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                            msg.exec_()
                            return
                    else:
                        if int(self.Window3.prun_acc_edit.text()) < 1 or int(self.Window3.prun_acc_edit.text()) > 20:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            
                            msg.setText("Enter a value for maximal accuracy loss between 1% and 20%")
                            msg.setWindowTitle("Warning")
                            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                            msg.exec_()
                            return
                    
                    self.prun_acc = int(self.Window3.prun_acc_edit.text())
                except:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    
                    msg.setText("Please enter a number for pruning or disable it.")
                    msg.setWindowTitle("Warning")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec_()
                    return

        if "Quantization" in self.optimizations and self.quant_dtype == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            
            msg.setText("Enter a dtype for quantization.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return
        
        if not self.optimizations:
            self.LoadWindow()
        else:
            self.DataloaderWindow()