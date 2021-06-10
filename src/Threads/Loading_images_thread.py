import sys
import time
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Loading_images(QThread):
    
    def __init__(self, Loadpng):
        QThread.__init__(self)
        self.Loadpng = Loadpng
        self.i = 0

    def run(self):
            
        while(self.isRunning()):
            
            if self.i < 15:
                self.i += 1
            else:
                self.i = 1
            
            time.sleep(0.75)
            
            self.Loadpng.setPixmap(QPixmap(os.path.join('src', 'GUILayout', 'Images','GUI_loading_images', 'GUI_load_' + str(self.i) + '.png')))
            
        
    def stop_thread(self):
        print(self.isRunning())
        print("Loading images thread end")
        self.terminate()