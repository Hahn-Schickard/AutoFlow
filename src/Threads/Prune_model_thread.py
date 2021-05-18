import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.Optimization.pruning import *


class Prune_model(QThread):
    
    request_signal = pyqtSignal()
    
    def __init__(self, datascript_path, model_path, prun_factor_dense, prun_factor_conv):
        QThread.__init__(self)
        self.datascript_path = datascript_path
        self.model_path = model_path
        self.prun_factor_dense = prun_factor_dense
        self.prun_factor_conv = prun_factor_conv
        

    def run(self):
          
        sys.path.append(os.path.dirname(self.datascript_path))
        datascript = __import__(os.path.splitext(os.path.basename(self.datascript_path))[0])
        
        x_train, y_train, x_test, y_test = datascript.get_data()
        pruned_model = pruning(self.model_path, x_train, y_train, self.prun_factor_dense, self.prun_factor_conv)
        pruned_model.save(str(self.model_path[:-3]) + '_pruned.h5', include_optimizer=False)
        self.request_signal.emit()
        
    def stop_thread(self):
        self.terminate()