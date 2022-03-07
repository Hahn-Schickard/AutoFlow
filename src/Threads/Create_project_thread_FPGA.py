'''Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

import sys
sys.path.append("..")   # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.Converter.create_project import *
import hls4ml


class ConvertBuildLoadingFPGA(QThread):
    """Thread to convert the model and build the project.

    Attributes:
        model_path:       Path of the model to convert
        project_name:     Name of the project to be created
        output_path:      Output path of the project to be created
    """

    request_signal = pyqtSignal()

    def __init__(self, model_path, project_name, output_path):
        QThread.__init__(self)
        self.model_path = model_path
        self.project_name = project_name
        self.output_path = output_path

    def run(self):
        """Activates the thread

        Calls the function to convert the model and build the FPGA
        project. When the function is finished, a signal is emitted.
        """
        print("Project name:", str(self.project_name))
        model = tf.keras.models.load_model(self.model_path)

        config = hls4ml.utils.config_from_keras_model(model,
                                                      granularity='model')

        hls_model = hls4ml.converters.convert_from_keras_model(
            model, hls_config=config, output_dir=str(self.output_path) + '/' +
            str(self.project_name))
        try:
            hls_model.compile()
        except:
            print("To compile the project, Xilinx has to be installed.")

        print("Ende")
        self.request_signal.emit()

    def stop_thread(self):
        """Ends the thread
        """
        self.terminate()
