''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UIAutoMLData(QWidget):
    """Select project name, output path and data path. 

    This GUI window has an input field and two buttons to pass
    project name, output path and data path.
    """
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, parent=None):
        super(UIAutoMLData, self).__init__(parent)
        
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE
        
        self.project_name_label = QLabel("AutoML Projectname:")
        self.project_name_label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        
        self.project_name = QLineEdit()
        self.project_name.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.project_name.setFixedWidth(0.25*self.WINDOW_WIDTH)
        
        self.output_path_label = QLabel("")
        self.output_path_label.setFixedWidth(0.7*self.WINDOW_WIDTH)
        self.output_path_label.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.output_path_label.setAlignment(Qt.AlignCenter)
        
        self.output_path_browse = QPushButton(" Output path... ", self)
        self.output_path_browse.setToolTip('Select a path where the AUTOFlow\n'
                                           'project should be stored.')
        self.output_path_browse.setStyleSheet("""QPushButton {
                           font: """ + str(int(0.035*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""")
        
        self.data_label = QLabel("Training data:")
        self.data_label.setStyleSheet("font: " + str(int(0.035*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        
        self.data_png = QLabel(self)
        self.data_png.setFixedWidth(0.25*self.WINDOW_HEIGHT)
        self.data_png.setFixedHeight(0.25*self.WINDOW_HEIGHT)
        data_img = QPixmap(os.path.join('src','GUILayout','Images','Database.png'))
        self.data_png.setPixmap(data_img)
        self.data_png.setScaledContents(True)
        
        self.data_path_label = QLabel("")
        self.data_path_label.setFixedWidth(0.7*self.WINDOW_WIDTH)
        self.data_path_label.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.data_path_label.setAlignment(Qt.AlignCenter)

        self.dataloader_list = QComboBox()
        self.dataloader_list.setFixedWidth(0.21*self.WINDOW_WIDTH)
        self.dataloader_list.addItems(["Select PATH with data", "Select FILE with data"])
        self.dataloader_list.setStyleSheet("font: " + str(int(0.023*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        
        self.select_data_browse = QPushButton(" Select Data... ", self)
        self.select_data_browse.setFixedWidth(0.2*self.WINDOW_WIDTH)
        self.select_data_browse.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.select_data_browse.setToolTip('Select the training data which the neural network requires for the optimization.\n'
                                              'The data can be transferred in different ways:\n'
                                              '- PATH (folder):\tImages are to be used as training data. In the given path there are\n'
                                              '\t\tsubfolders containing the name of the different classes of the neural\n'
                                              '\t\tnetwork and the corresponding images.\n'
                                              '- FILE (*.csv):\tThe data is stored in a CSV file.\n'
                                              '- FILE (*.py):\tThe data is loaded and returned in a Python script. It\n'
                                              '\t\tis important that the Python script contains the function\n'
                                              '\t\tget_data() with the return values x_train, y_train, x_test,\n'
                                              '\t\ty_test (training data, training label, test data, test label).\n'
                                              '\t\tThe return values here are Numpy arrays.')
        self.select_data_browse.setStyleSheet("""QPushButton {
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
        step_img = QPixmap(os.path.join('src','GUILayout','Images','GUI_progress_bar','GUI_train_step_2.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)

        self.next = QPushButton(self)
        self.next.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'next_arrow.png')))
        self.next.setIconSize(QSize(0.04*self.WINDOW_HEIGHT, 0.04*self.WINDOW_HEIGHT))
        self.next.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        
        self.back = QPushButton(self)
        self.back.setIcon(QIcon(os.path.join('src','GUILayout','Images', 'back_arrow.png')))
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
        self.horizontal_box[4].addWidget(self.output_path_browse)
        self.horizontal_box[4].setAlignment(Qt.AlignCenter)
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addItem(QSpacerItem(0.03*self.WINDOW_WIDTH, 0.03*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[6].addStretch()
        self.horizontal_box[6].addWidget(self.data_label)
        self.horizontal_box[6].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[7].addStretch()
        self.horizontal_box[7].addWidget(self.data_png)
        self.horizontal_box[7].addStretch()     
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[8].addStretch()
        self.horizontal_box[8].addWidget(self.data_path_label)
        self.horizontal_box[8].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[9].addStretch()
        self.horizontal_box[9].addWidget(self.dataloader_list)
        self.horizontal_box[9].addStretch()
        
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[10].addStretch()
        self.horizontal_box[10].addWidget(self.select_data_browse)
        self.horizontal_box[10].addStretch()
    
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[11].addItem(QSpacerItem(0.03*self.WINDOW_WIDTH, 0.03*self.WINDOW_HEIGHT))
        
        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.back, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.step, 0, 1)
        sublayout.addWidget(self.next, 0, 2, Qt.AlignRight)
        self.horizontal_box[12].addLayout(sublayout)
        self.horizontal_box[12].setAlignment(Qt.AlignBottom)
        
        
        self.vertical_box = QVBoxLayout()
        for i in range(0,len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])
        
        self.setLayout(self.vertical_box)