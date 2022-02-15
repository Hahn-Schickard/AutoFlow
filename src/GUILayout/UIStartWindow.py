''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UIStartWindow(QWidget):
    """Select project name, output path and model path. 

    This GUI window has an input field and two buttons to pass
    project name, output path and model path.
    """
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, parent=None):
        super(UIStartWindow, self).__init__(parent)
        
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE

        self.project_name_label = QLabel("Projectname:")
        self.project_name_label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)

        self.project_name = QLineEdit()
        self.project_name.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.project_name.setFixedWidth(0.25*self.WINDOW_WIDTH)
        
        self.output_path_label = QLabel("")
        self.output_path_label.setFixedWidth(0.7*self.WINDOW_WIDTH)
        self.output_path_label.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.output_path_label.setAlignment(Qt.AlignCenter)
        
        self.output_path_Browse = QPushButton(" Output path... ", self)
        self.output_path_Browse.setFixedWidth(0.2*self.WINDOW_WIDTH)
        self.output_path_Browse.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.output_path_Browse.setToolTip('Select a path where the TFL2uC\n'
                                           'project should be stored.')
        self.output_path_Browse.setStyleSheet("""QPushButton {
                           font: """ + str(int(0.035*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""")

        self.keras_model_label = QLabel("Keras model:")
        self.keras_model_label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)  

        self.Modelpng = QLabel(self)
        self.Modelpng.setFixedWidth(0.25*self.WINDOW_HEIGHT)
        self.Modelpng.setFixedHeight(0.25*self.WINDOW_HEIGHT)
        Modelimg = QPixmap(os.path.join('src','GUILayout','Images','network.png'))
        self.Modelpng.setPixmap(Modelimg)
        self.Modelpng.setScaledContents(True)
        
        self.model_path_label = QLabel("")
        self.model_path_label.setFixedWidth(0.7*self.WINDOW_WIDTH)
        self.model_path_label.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.model_path_label.setAlignment(Qt.AlignCenter)
        
        self.select_model_browse = QPushButton(" Select Model... ", self)
        self.select_model_browse.setFixedWidth(0.2*self.WINDOW_WIDTH)
        self.select_model_browse.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.select_model_browse.setToolTip('Select a TensorFlow/Keras model (.h5 file)\n'
                                          'which should be converted to a TensorFlow\n'
                                          'Lite C++ file, to execute it on a MCU')
        self.select_model_browse.setStyleSheet("""QPushButton {
                           font: """ + str(int(0.035*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""")
        
        self.step = QLabel(self)
        self.step.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        step_img = QPixmap(os.path.join('src','GUILayout','Images','GUI_progress_bar','GUI_step_2.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter) 

        self.next = QPushButton(self)
        self.next.setIcon(QIcon(os.path.join('src','GUILayout','Images','next_arrow.png')))
        self.next.setIconSize(QSize(0.04*self.WINDOW_HEIGHT, 0.04*self.WINDOW_HEIGHT))
        self.next.setFixedHeight(0.05*self.WINDOW_HEIGHT)

        self.back = QPushButton(self)
        self.back.setIcon(QIcon(os.path.join('src','GUILayout','Images','back_arrow.png')))
        self.back.setIconSize(QSize(0.04*self.WINDOW_HEIGHT, 0.04*self.WINDOW_HEIGHT))
        self.back.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        
        
        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].addWidget(self.project_name_label)
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].setAlignment(Qt.AlignTop)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addWidget(self.project_name)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addItem(QSpacerItem(0.03*self.WINDOW_WIDTH, 0.03*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addWidget(self.output_path_label)
        self.horizontal_box[3].setAlignment(Qt.AlignCenter)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addWidget(self.output_path_Browse)
        self.horizontal_box[4].setAlignment(Qt.AlignCenter)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addItem(QSpacerItem(0.03*self.WINDOW_WIDTH, 0.03*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[6].addStretch()
        self.horizontal_box[6].addWidget(self.keras_model_label)
        self.horizontal_box[6].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[7].addStretch()
        self.horizontal_box[7].addWidget(self.Modelpng)
        self.horizontal_box[7].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[8].addItem(QSpacerItem(0.03*self.WINDOW_WIDTH, 0.03*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[9].addStretch()
        self.horizontal_box[9].addWidget(self.model_path_label)
        self.horizontal_box[9].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[10].addStretch()
        self.horizontal_box[10].addWidget(self.select_model_browse)
        self.horizontal_box[10].addStretch()
    
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[11].addItem(QSpacerItem(0.08*self.WINDOW_WIDTH, 0.08*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.back, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.step, 0, 1, Qt.AlignCenter)
        sublayout.addWidget(self.next, 0, 2, Qt.AlignRight)
        self.horizontal_box[12].addLayout(sublayout)
        self.horizontal_box[12].setAlignment(Qt.AlignBottom)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)