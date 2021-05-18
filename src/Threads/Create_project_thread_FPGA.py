import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.Converter.create_project import *
import subprocess as sub
import hls4ml



class Convert_Build_Loading_FPGA(QThread):
    
    request_signal = pyqtSignal()
    
    def __init__(self, model_path, project_name, output_path):
        QThread.__init__(self)
        self.model_path = model_path
        self.project_name = project_name
        self.output_path = output_path
        

    def run(self):
        print(str(self.project_name))
        model = tf.keras.models.load_model(self.model_path)
        
        config = hls4ml.utils.config_from_keras_model(model, granularity='model')
        
        
        hls_model = hls4ml.converters.convert_from_keras_model(model, hls_config=config, output_dir=str(self.output_path)+'/'+str(self.project_name))
        hls_model.compile()
        
        print("Ende")
        self.request_signal.emit()
        
    def stop_thread(self):
        self.terminate()
