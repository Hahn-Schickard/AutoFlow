''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

"""This is a splittet method from the Mainwindow class which contain the logic for the SettingsWindow window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
from src.GUILayout.UISettingsWindow import *
        
def SettingsWindow(self):
    """Define Logic for the SettingsWindow GUI

    Retrieves the parameter class and set the data path, project path and output path

    Args:
      self:
        self represents the instance of the class.
      parameter:
        A parameter class with all the parameter we change and need to start the project
      

    Returns:


    Raises:
      IOError: An error occurred accessing the parameterset.
    """     
    self.Window4 = UISettingsWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self.task, self)
    
    self.Window4.epochs_factor.setText(str(self.max_epoch))
    self.Window4.max_trials_factor.setText(str(self.max_trials))
    self.Window4.max_size_factor.setText(str(self.max_size))
    self.Window4.num_channels.setText(str(self.num_channels))
    self.Window4.img_height.setText(str(self.img_height))
    self.Window4.img_width.setText(str(self.img_width))
    
    self.Window4.back.clicked.connect(lambda:nextWindow(self,"Back"))
    self.Window4.next.clicked.connect(lambda:nextWindow(self,"Next"))
    
    
    self.setCentralWidget(self.Window4)
    self.show()



def nextWindow(self,n):
    """
    Defines which one is the next window to open.

    Args:
        n:  Go forward or go back
    """

    if n == "Back":
        self.TaskWindow()

    elif n == "Next":
        try:
            self.max_epoch = int(self.Window4.epochs_factor.text())
            self.max_trials = int(self.Window4.max_trials_factor.text())
            self.max_size = int(self.Window4.max_size_factor.text())
            self.num_channels = int(self.Window4.num_channels.text())
            self.img_height = int(self.Window4.img_height.text())
            self.img_width = int(self.Window4.img_width.text())
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
                
            msg.setText("Please enter a valid number for all parameters.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return


        reply = QMessageBox.question(self, 'Start training', 'Do you want to start model training?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.ReturnWindow()
        else:
            return
