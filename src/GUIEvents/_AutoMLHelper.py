import sys
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

    if self.target == "imageClassification":
        os.system(
            f"start /B start cmd.exe @cmd /k python autoML/ImageClassifier.py --ProjectName={self.project_name} --OutputPath={self.output_path_ml} --DataPath={self.data_loader_path_ml} --ParamConstraint={self.params_check} --ParamFactor={self.params_factor} --FlopConstraint={self.floats_check} --FlopFactor={self.floats_factor} --ComplexConstraint={self.complex_check} --ComplexFactor={self.complex_factor} --MaxSize={self.max_size} --MaxTrials={self.max_trials} --MaxEpochs={self.max_epoch}"
        )

    if self.target == "imageRegression":
        os.system(
            f"start /B start cmd.exe @cmd /k python autoML/ImageRegressor.py --ProjectName={self.project_name} --OutputPath={self.output_path_ml} --DataPath={self.data_loader_path_ml} --ParamConstraint={self.params_check} --ParamFactor={self.params_factor} --FlopConstraint={self.floats_check} --FlopFactor={self.floats_factor} --ComplexConstraint={self.complex_check} --ComplexFactor={self.complex_factor} --MaxSize={self.max_size} --MaxTrials={self.max_trials} --MaxEpochs={self.max_epoch}"
        )


def get_output_path_ml(self, CurWindow):
    self.output_path_ml = QFileDialog.getExistingDirectory(
        self, "Select the output path", "./"
    )
    CurWindow.Output_Pfad.setText(self.output_path_ml)
    print(CurWindow.Output_Pfad.text())


def get_data_loader_path_ml(self, CurWindow):
    self.data_loader_path_ml = QFileDialog.getOpenFileName(
        self, "Select your data loader script", "./"
    )[0]
    CurWindow.Daten_Pfad.setText(self.data_loader_path_ml)
    print(CurWindow.Daten_Pfad.text())


def set_params(self):
    if self.Window3.Params.isChecked() == True:
        if not "Params" in self.constraints:
            self.constraints.append("Params")
            print(self.constraints)
        if self.params_factor == None:
            self.Window3.Params_factor.setText("1")
        else:
            self.Window3.Params_factor.setText(str(self.params_factor))
        self.Window3.Params_factor.setVisible(True)
        self.Window3.Params_label.setVisible(True)

        self.Window3.Params.setIconSize(QSize(100, 100))
        self.Window3.Params.setGeometry(145, 85, 120, 120)

    else:
        if "Params" in self.constraints:
            self.constraints.remove("Params")
            print(self.constraints)
        self.params_factor = float(self.Window3.Params_factor.text())
        self.Window3.Params_factor.setVisible(False)
        self.Window3.Params_label.setVisible(False)

        self.Window3.Params.setIconSize(QSize(150, 150))
        self.Window3.Params.setGeometry(120, 85, 170, 170)


def set_floats(self):
    if self.Window3.Floats.isChecked() == True:
        if not "Floats" in self.constraints:
            self.constraints.append("Floats")
            print(self.constraints)
        if self.floats_factor == None:
            self.Window3.Floats_factor.setText("1")
        else:
            self.Window3.Floats_factor.setText(str(self.floats_factor))
        self.Window3.Floats_factor.setVisible(True)
        self.Window3.Floats_label.setVisible(True)

        self.Window3.Floats.setIconSize(QSize(100, 100))
        self.Window3.Floats.setGeometry(540, 85, 120, 120)

    else:
        if "Floats" in self.constraints:
            self.constraints.remove("Floats")
            print(self.constraints)
        self.floats_factor = float(self.Window3.Floats_factor.text())
        self.Window3.Floats_factor.setVisible(False)
        self.Window3.Floats_label.setVisible(False)

        self.Window3.Floats.setIconSize(QSize(150, 150))
        self.Window3.Floats.setGeometry(515, 85, 170, 170)


def set_complex(self):
    if self.Window3.Complex.isChecked() == True:
        if not "Complex" in self.constraints:
            self.constraints.append("Complex")
            print(self.constraints)
        if self.complex_factor == None:
            self.Window3.Complex_factor.setText("1")
        else:
            self.Window3.Complex_factor.setText(str(self.complex_factor))
        self.Window3.Complex_factor.setVisible(True)
        self.Window3.Complex_label.setVisible(True)

        self.Window3.Complex.setIconSize(QSize(100, 100))
        self.Window3.Complex.setGeometry(145, 320, 120, 120)

    else:
        if "Complex" in self.constraints:
            self.constraints.remove("Complex")
            print(self.constraints)
        self.complex_factor = float(self.Window3.Complex_factor.text())
        self.Window3.Complex_factor.setVisible(False)
        self.Window3.Complex_label.setVisible(False)

        self.Window3.Complex.setIconSize(QSize(150, 150))
        self.Window3.Complex.setGeometry(120, 320, 170, 170)


def Form_clicked(self):
    self.X = 0
    self.Y = 0

    self.Dot.setVisible(True)
    if self.Window3a.Parameter.text() == "":
        Parameter = 0

    else:
        Parameter = self.Window3a.Parameter.text()
        print(type(Parameter))
        try:
            Parameter = int(Parameter)
        except ValueError:
            self.Window3a.Parameter.setText(Parameter[:-1])
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("Please enter a number not a character.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return

    if self.Window3a.FPS.text() == "":
        FPS = 0

    else:
        FPS = self.Window3a.FPS.text()
        try:
            FPS = int(FPS)
        except ValueError:
            self.Window3a.FPS.setText(FPS[:-1])
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("Please enter a number not a character.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return

    FLOPs = Parameter * FPS
    print(FLOPs)

    if FLOPs < 10000000000:
        self.Y = 100
    if FLOPs > 100000000000:
        self.Y -= 100

    if self.Window3a.Forms.isChecked():
        self.Y = 100

    if self.Window3a.Forml.isChecked():
        self.Y = -100

    if self.Window3a.Flexs.isChecked():
        self.X = 200

    if self.Window3a.Flexl.isChecked():
        self.X = -200

    if self.Window3a.Energies.isChecked():
        self.Y = 50
        self.X = 50

    if self.Window3a.Energiel.isChecked():
        self.Y = -50
        self.X = -50

    if self.Window3a.Preiss.isChecked():
        self.Y = 50
        self.X = 50

    if self.Window3a.Preisl.isChecked():
        self.Y = -50
        self.X = -50

    if self.Window3a.Preism.isChecked():
        if self.X > 0:
            self.X -= 25
        if self.X < 0:
            self.X = 25
        if self.Y > 0:
            self.Y -= 25
        if self.Y < 0:
            self.Y = 25

    if self.Window3a.Energiem.isChecked():
        if self.X > 0:
            self.X -= 25
        if self.X < 0:
            self.X = 25
        if self.Y > 0:
            self.Y -= 25
        if self.Y < 0:
            self.Y = 25

    if self.Window3a.Formm.isChecked():
        if self.Y > 0:
            self.Y -= 25
        if self.Y < 0:
            self.Y = 25

    if self.Window3a.Flexm.isChecked():
        if self.X > 0:
            self.X -= 100
        if self.X < 0:
            self.X = 100

    print("vor:")
    print("y")
    print(self.Y)
    print("x")
    print(self.X)

    if self.Y > 200:
        self.Y = 200
    if self.Y < -200:
        self.Y = -200

    if self.X > 200:
        self.X = 200
    if self.X < -200:
        self.X = -200

    if self.X > 0:
        self.X = self.X - ((math.sqrt(self.Y * self.Y)) * 0.5)
    if self.X < 0:
        self.X = self.X((math.sqrt(self.Y * self.Y)) * 0.5)

    print("y")
    print(self.Y)
    print("x")
    print(self.X)

    self.update_draw(self.X, self.Y)


# 11Tflops
# 1GF

        
def update_draw(self,x,y):
    x=390+x
    y=540+y
    
    self.Dot.move(x,y)
                