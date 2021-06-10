import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.Threads.Loading_images_thread import * 
from src.Threads.Create_project_thread import *
from src.Threads.Create_project_thread_FPGA import *
from src.Threads.Prune_model_thread import *



class UILoadWindow(QWidget):
    def __init__(self, FONT_STYLE, model_path, project_name, output_path, datascript_path, prun_factor_dense, prun_factor_conv, optimizations, quant_dtype, target, parent=None):
        super(UILoadWindow, self).__init__(parent)
        
        self.FONT_STYLE = FONT_STYLE        
        self.project_name = project_name
        self.model_path = model_path
        self.output_path = output_path
        self.datascript_path = datascript_path
        self.model_path = model_path
        self.prun_factor_dense = prun_factor_dense
        self.prun_factor_conv = prun_factor_conv
        self.target=target
        self.optimizations = optimizations
        self.quant_dtype = quant_dtype
        
        
        self.label = QLabel("Create Projectfiles")
        self.label.setStyleSheet("font: 12pt " + FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.Abstand = QLabel()
        self.Abstand.setFixedHeight(30)
        
        self.Loadpng = QLabel(self)
        img = QPixmap(os.path.join('src','GUILayout','Images','GUI_loading_images', 'GUI_load_0.png'))
        self.Loadpng.setPixmap(img)
        
        self.Schritt = QLabel(self)
        Schritt_img = QPixmap(os.path.join('src','GUILayout','Images', 'GUI_progress_bar', 'GUI_step_7.png'))
        self.Schritt.setPixmap(Schritt_img)
        self.Schritt.setFixedHeight(30)
        self.Schritt.setAlignment(Qt.AlignCenter)
        
        self.Finish = QPushButton("Finish", self)
        self.Finish.setFixedWidth(125)
        self.Finish.setVisible(False)
        self.Finish.setToolTip('...')
        self.Finish.setStyleSheet("""QPushButton {
                           font: 12pt """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""") 
        
        self.Back = QPushButton(self)
        self.Back.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'back_arrow.png')))
        self.Back.setIconSize(QSize(25, 25))
        self.Back.setFixedHeight(30)

        self.Load = QPushButton(self)
        self.Load.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'load_arrow.png')))
        self.Load.setIconSize(QSize(25, 25))
        self.Load.setFixedHeight(30)
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.Loadpng)
        self.horizontal_box[1].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addWidget(self.Finish)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addWidget(self.Back)
        self.horizontal_box[3].addStretch()
        self.horizontal_box[3].addWidget(self.Schritt) 
        self.horizontal_box[3].addStretch()         
        self.horizontal_box[3].addWidget(self.Load)
        self.horizontal_box[3].setAlignment(Qt.AlignBottom)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)
        
        self.loading_images = Loading_images(self.Loadpng)
        
        self.prune_model = Prune_model(self.datascript_path, self.model_path, self.prun_factor_dense, self.prun_factor_conv, self.optimizations)

        
        if 'uC' in target:
            if 'Pruning' in optimizations:
                self.conv_build_load = Convert_Build_Loading(str(self.model_path[:-3]) + '_pruned.h5', self.project_name, self.output_path, self.optimizations, self.datascript_path, self.quant_dtype)
            else:
                self.conv_build_load = Convert_Build_Loading(self.model_path, self.project_name, self.output_path, self.optimizations, self.datascript_path, self.quant_dtype)
        if 'FPGA' in target:
            self.conv_build_load = Convert_Build_Loading_FPGA(self.model_path, self.project_name, self.output_path, self.optimizations, self.datascript_path, self.quant_dtype)
            