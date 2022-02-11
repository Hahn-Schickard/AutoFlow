''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

"""This is a splittet method from the Mainwindow class which contain the logic for the ReturnWindow window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""

from src.GUILayout.UIReturnWindow import *


        
def ReturnWindow(self):  
    """Define Logic for the ReturnWindow GUI

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
    
    self.Window6 = UIReturnWindow(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self)
    
    self.Window6.back.clicked.connect(lambda:nextWindow(self,"Back"))
    self.Window6.Load.clicked.connect(lambda:nextWindow(self,"Next"))    

    self.setCentralWidget(self.Window6)
    self.show()



def nextWindow(self,n):

    if n == "Back":
        self.AutoMLWindow()

    elif n == "Next":
        self.GUIStart()