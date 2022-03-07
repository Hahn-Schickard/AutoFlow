'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

import os
import sys
sys.path.append("..")   # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UIGUIStart(QWidget):
    """Start window of the GUI

    This window has two buttons to choose if you want
    to train a new model or load a trained one.
    """
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, parent=None):
        super(UIGUIStart, self).__init__(parent)

        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE

        self.label = QLabel("Load or train a model?")
        self.label.setStyleSheet(
            "font: " + str(int(0.035 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)

        self.step = QLabel(self)
        self.step.setFixedHeight(0.05 * self.WINDOW_HEIGHT)
        step_img = QPixmap(os.path.join(
            'src', 'gui_layout', 'images', 'gui_progress_bar',
            'GUI_step_1.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)

        self.label_train_model = QLabel("Train a new model")
        self.label_train_model.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.label_train_model.setFixedWidth(0.35 * self.WINDOW_WIDTH)
        self.label_train_model.setAlignment(Qt.AlignCenter)

        self.train_model = QPushButton(self)
        self.train_model.setIcon(QIcon(os.path.join(
            'src', 'gui_layout', 'images', 'Trainmodel.png')))
        self.train_model.setIconSize(QSize(0.2 * self.WINDOW_WIDTH,
                                           0.30 * self.WINDOW_HEIGHT))
        self.train_model.setToolTip('Train a new TensorFlow model by using '
                                    'AutoKeras.')
        self.train_model.setStyleSheet(
            """QPushButton {
            font: """ + str(int(0.035 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
            QPushButton::hover {
            background-color : rgb(10, 100, 200)}
            QToolTip {
            font: """ + str(int(0.025 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
            background-color : rgb(53, 53, 53);
            color: white;
            border: black solid 1px}""")
        self.train_model.setFixedHeight(0.35 * self.WINDOW_HEIGHT)
        self.train_model.setFixedWidth(0.35 * self.WINDOW_WIDTH)

        self.label_load_model = QLabel("Load a trained model")
        self.label_load_model.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.label_load_model.setFixedWidth(0.35 * self.WINDOW_WIDTH)
        self.label_load_model.setAlignment(Qt.AlignCenter)

        self.load_model = QPushButton(self)
        self.load_model.setIcon(QIcon(os.path.join(
            'src', 'gui_layout', 'images', 'Loadmodel.png')))
        self.load_model.setIconSize(QSize(0.2 * self.WINDOW_WIDTH,
                                          0.3 * self.WINDOW_HEIGHT))
        self.load_model.setToolTip(
            'Load an already trained TensorFlow model and\n'
            'convert it for a device of your choice.')
        self.load_model.setStyleSheet(
            """QPushButton {
            font: """ + str(int(0.035 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
            QPushButton::hover {
            background-color : rgb(10, 100, 200)}
            QToolTip {
            font: """ + str(int(0.025 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
            background-color : rgb(53, 53, 53);
            color: white;
            border: black solid 1px}""")
        self.load_model.setFixedHeight(0.35 * self.WINDOW_HEIGHT)
        self.load_model.setFixedWidth(0.35 * self.WINDOW_WIDTH)

        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].setAlignment(Qt.AlignTop)

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.label_train_model)
        self.horizontal_box[1].addStretch()
        self.horizontal_box[1].addWidget(self.label_load_model)
        self.horizontal_box[1].addStretch()

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addStretch()
        self.horizontal_box[2].addWidget(self.load_model)
        self.horizontal_box[2].addStretch()
        self.horizontal_box[2].addWidget(self.train_model)
        self.horizontal_box[2].addStretch()

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addItem(QSpacerItem(
            0.25 * self.WINDOW_WIDTH, 0.25 * self.WINDOW_HEIGHT))

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addStretch()
        self.horizontal_box[4].addWidget(self.step)
        self.horizontal_box[4].addStretch()

        self.vertical_box = QVBoxLayout()
        for i in range(0, len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])

        self.setLayout(self.vertical_box)
