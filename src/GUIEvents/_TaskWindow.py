''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

"""This is a splittet method from the Mainwindow class which contain the logic for the TaskWindow window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
from src.GUILayout.UITaskWindow import *

        
def TaskWindow(self):
    """Define Logic for the TaskWindow GUI

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
    
    self.Window2 = UITaskWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self)
    
    
    self.Window2.ImageClassification.clicked.connect(lambda:nextWindow(self,"Next","imageClassification"))
    self.Window2.ImageRegression.clicked.connect(lambda:nextWindow(self,"Next","imageRegression"))
    self.Window2.TextClassification.clicked.connect(lambda:nextWindow(self,"Next","textClassification"))
    self.Window2.TextRegression.clicked.connect(lambda:nextWindow(self,"Next","textRegression"))
    self.Window2.DataClassification.clicked.connect(lambda:nextWindow(self,"Next","dataClassification"))
    self.Window2.DataRegression.clicked.connect(lambda:nextWindow(self,"Next","dataRegression"))

    
    self.Window2.back.clicked.connect(lambda:nextWindow(self,"Back",None))
    
    self.setCentralWidget(self.Window2)
    self.show()



def nextWindow(self,n,task):

    if n == "Back":
        self.AutoMLData()

    elif n == "Next":
        self.task = task
        print(self.task)

        if self.task == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
             
            msg.setText("Please choose a task")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            return

        self.SettingsWindow()