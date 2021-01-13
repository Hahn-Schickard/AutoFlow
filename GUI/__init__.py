import sys
import os


import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    from ._MarcusWindow1 import MarcusWindow1
    from ._MarcusWindow2 import MarcusWindow2
    from ._MarcusWindow3 import MarcusWindow3
    from ._MarcusWindow4 import MarcusWindow4
    from ._MarcusWindow5 import MarcusWindow5
    from ._HelperWindow import HelperWindow
    from ._LoadWindow import LoadWindow
    from ._OptiWindow import OptiWindow

    # from ._RestrictionWindow import RestrictionWindow
    from ._SettingsWindow import SettingsWindow
    from ._StartWindow import StartWindow
    from ._TargetWindow import TargetWindow
    from ._TaskWindow import TaskWindow
    from ._ConstraintsWindow import ConstraintsWindow
    from ._ReturnWindow import ReturnWindow
    from ._AutoMLWindow import AutoMLWindow

    from ._AutoMLHelper import (
        start_autokeras,
        get_output_path_ml,
        get_data_loader_path_ml,
        Form_clicked,
        update_draw,
        set_floats,
        set_complex,
        set_params,
    )
    from ._Helper import (
        get_output_path,
        get_model_path,
        get_data_loader_path,
        set_pruning,
        set_quantization,
        set_quant_dtype,
        set_knowledge_distillation,
        set_huffman_coding,
        get_optimization,
        set_optimizations,
        model_pruning,
        download,
        terminate_thread,
        optimization_before_load
    )

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Neural Network on Microcontroller")
        self.setWindowIcon(QIcon(os.path.join("Images", "Window_Icon_blue.png")))
        self.setFixedWidth(800)
        self.setFixedHeight(600)

        self.FONT_STYLE = "Helvetica"

        self.X = 0
        self.Y = 0
        self.project_name = None
        self.output_path = None
        self.output_path_ml = None
        self.model_path = None
        self.data_loader_path = None
        self.data_loader_path_ml = None
        self.target = None
        self.optimizations = []
        self.constraints = []

        self.prun_factor_dense = None
        self.prun_factor_conv = None
        self.quant_dtype = None
        self.Know_Dis_1 = None
        self.Know_Dis_2 = None
        self.Huffman_1 = None
        self.Huffman_2 = None

        self.params_factor = 1
        self.floats_factor = 1
        self.complex_factor = 1
        self.max_size = 0
        self.max_trials = 10
        self.max_epoch = 20

        self.params_check = False
        self.floats_check = False
        self.complex_check = False

        self.MarcusWindow1()

    