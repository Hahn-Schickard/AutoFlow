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
        self.image_number = 0

    def run(self):
            
        while(self.isRunning()):
            
            if self.image_number < 15:
                self.image_number += 1
            else:
                self.image_number = 1
            
            time.sleep(0.75)
            
            self.Loadpng.setPixmap(QPixmap(os.path.join('src', 'GUILayout', 'Images','GUI_loading_images', 'GUI_load_' + str(self.image_number) + '.png')))
            
        
    def stop_thread(self):
        print(self.isRunning())
        print("Loading images thread end")
        self.terminate()