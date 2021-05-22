"""This is a splittet method from the Mainwindow class which contain the logic for the AutoMLData window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
from src.GUILayout.UISettingsWindow import *
        
def SettingsWindow(self, n):     
                  
    
    if n == "Next":
        if "Params" in self.constraints:
            try:
                print(float(self.Window3.Params_factor.text()))
                if float(self.Window3.Params_factor.text()) < 0.1 or float(self.Window3.Params_factor.text()) > 10:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                     
                    msg.setText("Enter factor between 0.1 and 10")
                    msg.setWindowTitle("Warning")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec_()
                    return
                
                self.params_factor = float(self.Window3.Params_factor.text())
            except:                    
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                 
                msg.setText("Please enter a number")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
                return
        
        if "Floats" in self.constraints:
            try:
                print(float(self.Window3.Floats_factor.text()))
                if float(self.Window3.Floats_factor.text()) < 0.1 or float(self.Window3.Floats_factor.text()) > 10:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                     
                    msg.setText("Enter factor between 0.1 and 10")
                    msg.setWindowTitle("Warning")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec_()
                    return
                
                self.floats_factor = float(self.Window3.Floats_factor.text())
            except:                    
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                 
                msg.setText("Please enter a number")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
                return
            
        if "Complex" in self.constraints:
            try:
                print(float(self.Window3.Complex_factor.text()))
                if float(self.Window3.Complex_factor.text()) < 0.1 or float(self.Window3.Complex_factor.text()) > 10:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                     
                    msg.setText("Enter factor between 0.1 and 10")
                    msg.setWindowTitle("Warning")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.exec_()
                    return
                
                self.complex_factor = float(self.Window3.Complex_factor.text())
            except:                    
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                 
                msg.setText("Please enter a number")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.exec_()
                return
        

    self.Window4 = UISettingsWindow(self.FONT_STYLE, self)
    

    self.Window4.epochs_factor.setText(str(self.max_epoch))
    self.Window4.max_trials_factor.setText(str(self.max_trials))
    self.Window4.max_size_factor.setText(str(self.max_size))
    
    self.Window4.Back.clicked.connect(lambda:self.ConstraintsWindow("Back", self.target))
    self.Window4.Next.clicked.connect(lambda:self.AutoMLWindow("Next"))
    
    
    self.setCentralWidget(self.Window4)
    self.show()