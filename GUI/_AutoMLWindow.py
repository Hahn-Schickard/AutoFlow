import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UIWindows.UIAutoMLWindow import *

   
def AutoMLWindow(self, n):         
    if n == "Next":
        self.max_epoch = self.Window4.epochs_factor.text()
        self.max_trials = self.Window4.max_trials_factor.text()
        self.max_size = self.Window4.max_size_factor.text()

    
    self.Window5 = UIAutoMLWindow(self.FONT_STYLE, self)
      
    self.Window5.Back.clicked.connect(lambda:self.SettingsWindow("Back"))
    self.Window5.Start.clicked.connect(lambda:self.ReturnWindow("Next"))
   
    self.Window5.Finish.clicked.connect(self.close)

    
    self.setCentralWidget(self.Window5)
    self.show()