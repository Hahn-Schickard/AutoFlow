''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

from src.GUILayout.Start import *


def GUIStart(self):
    """Define Logic for the GUIStart GUI

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
    
    
    self.GUIStart1 = UIMarcusWindow1(self.WINDOW_WIDTH, self.WINDOW_HEIGHT, self.FONT_STYLE, self)
    
    self.GUIStart1.load_model.clicked.connect(lambda:nextWindow(self,"AutoML"))
    self.GUIStart1.train_model.clicked.connect(lambda:nextWindow(self,"LoadModel"))
    
    self.setCentralWidget(self.GUIStart1)
    self.show()



def nextWindow(self,n):
    """
    Defines which one is the next window to open.

    Args:
        n:  Next window to open
    """
    if n == "AutoML":
        self.AutoMLData()

    elif n == "LoadModel":
        self.StartWindow()