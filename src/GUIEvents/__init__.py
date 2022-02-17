''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    """Initialization of the GUI main window.

    All initializations of the different GUI windows get imported.
    Also all functions get from the '_Helper.py' file imported.
    The window size and title get initialized as well as all attributes
    needed. In addition, the GUI is started.

    Attributes:
        FONT_STYLE:           Font which is used in the GUI
        WINDOW_WIDTH:         Width of the GUI window
        WINDOW_HEIGHT:        Height of the GUI window
        project_name:         Name of the project to be created
        output_path:          Output path of the project to be created
        model_path:           Path of the model to convert
        data_loader_path:     Path of the folder or file with the training data
        target:               Target to execute the neural network
        optimizations:        Selected optimization algorithms
        prun_type:            Pruning type to optimize the model
        prun_factor_dense:    Pruning factor for fully connected layers
        prun_factor_conv:     Pruning factor for convolution layers
        prun_acc_type:        Type of accuracy pruning
        prun_acc:             Accuracy for model pruning
        quant_dtype:          Data type to quantize to
        task:                 The model type to interpret the data
        max_trials:           The maximum number of attempts for AutoKeras to find the best model
        max_epochs:            Number of maximal training epochs
        max_size:             The maximum model size that AutoKeras is allowed to use.
        num_channels:         Number of channels of the inputdata for images
        img_height:           Height of the input images
        img_width:            Width of the input images
        separator:            Separator for reading a CSV file
        decimal:              Decimal for reading a CSV file
        csv_target_label:     Target label from the CSV file
        model_memory:         Memory to allocate for the model on a microcontroller


    """
    from ._Start import GUIStart
    from ._AutoMLData import AutoMLData
    from ._LoadWindow import LoadWindow
    from ._OptiWindow import OptiWindow
    from ._SettingsWindow import SettingsWindow
    from ._StartWindow import StartWindow
    from ._TargetWindow import TargetWindow
    from ._TaskWindow import TaskWindow
    from ._AutoMLWindow import AutoMLWindow
    from ._DataloaderWindow import DataloaderWindow
    from ._CSVDataloaderWindow import CSVDataloaderWindow

    from ._AutoMLHelper import (
        start_autokeras,
    )
    
    from ._GUIHelper import (
        get_output_path,
        get_model_path,
        get_data_loader,
        set_label,
        set_pruning,
        set_quantization,
        set_prun_type,
        set_prun_acc_type,
        set_quant_dtype,
        model_pruning,
        convert_create,
        terminate_thread,
        browse_csv_data,
        preview_csv_data,
        load_csv_data,
        get_separator
    )

    from ._DataloaderHelper import (
        dataloader_quantization,
        dataloader_pruning
    )

    def __init__(self, screen_width, screen_height, parent=None):
        """the init method for the GUI logic

    This method initialize the GUI and the config parameters 
    we need to execute the train/implement process
    
    Attributes:
        screen_width:   Width of the used monitor.
        screen_height:  Height of the used monitor.
    """
        super(MainWindow, self).__init__(parent)

        """Set width and height of the window in respect to the resolution of the screen
        """
        if screen_width/screen_height >= 2: #>= 2:1
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = int(0.4*screen_width), int(0.64*screen_height)
        elif screen_width/screen_height <= 0.5: #>= 2:1 Hochformat
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = int(0.85*screen_width), int(0.3*screen_height)
        elif abs(screen_width/screen_height - 4/3) < 0.1: #4:3
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = int(0.55*screen_width), int(0.5*screen_height)
        elif abs(screen_width/screen_height - 3/4) < 0.1: #4:3 Hochformat
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = int(0.75*screen_width), int(0.4*screen_height)
        elif abs(screen_width/screen_height - 16/10) < 0.1: #16:10
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = int(0.5*screen_width), int(0.6*screen_height)
        elif abs(screen_width/screen_height - 10/16) < 0.1: #16:10 Hochformat
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = int(0.8*screen_width), int(0.35*screen_height)
        else:
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT = int(0.45*screen_width), int(0.6*screen_height)

        self.setFixedSize(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        print("WINDOW_WIDTH:",self.WINDOW_WIDTH)
        print("WINDOW_HEIGHT:",self.WINDOW_HEIGHT)
        self.setWindowTitle("AUTOflow")
        self.setWindowIcon(QIcon(os.path.join("src", "GUILayout", "Images", "Window_Icon_blue.png")))

        self.FONT_STYLE = "Helvetica"

        self.project_name = None
        self.output_path = None
        self.model_path = None
        self.data_loader_path = None
        self.target = None
        self.optimizations = []

        self.prun_type = None
        self.prun_factor_dense = None
        self.prun_factor_conv = None
        self.prun_acc_type = None
        self.prun_acc = None
        self.quant_dtype = None
        
        self.task = None
        self.max_trials = 10
        self.max_epochs = 20
        self.max_size = 0
        self.num_channels = 3
        self.img_height = 128
        self.img_width = 128
        
        self.separator = None
        self.decimal = None
        self.csv_target_label = None

        self.model_memory = None

        self.GUIStart()