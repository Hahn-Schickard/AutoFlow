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
    self.Window4 = UISettingsWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self)
    

    self.Window4.epochs_factor.setText(str(self.max_epoch))
    self.Window4.max_trials_factor.setText(str(self.max_trials))
    self.Window4.max_size_factor.setText(str(self.max_size))
    
    self.Window4.Back.clicked.connect(lambda:nextWindow(self,"Back"))
    self.Window4.Next.clicked.connect(lambda:nextWindow(self,"Next"))
    
    
    self.setCentralWidget(self.Window4)
    self.show()



def nextWindow(self,n):

    if n == "Back":
        self.TaskWindow()

    elif n == "Next":
        self.max_epoch = self.Window4.epochs_factor.text()
        self.max_trials = self.Window4.max_trials_factor.text()
        self.max_size = self.Window4.max_size_factor.text()

        self.AutoMLWindow()