'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Marcel Sawrin + Marcus Rueb
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UIAutoMLTask(QWidget):
    """Select the task to interpret the data.

    In this window you can choose on which task the neural network
    should execute. You can choose the task by clicking the
    corresponding button.
    """
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, parent=None):
        super(UIAutoMLTask, self).__init__(parent)

        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE

        self.label = QLabel("Choose your Task")
        self.label.setStyleSheet(
            "font: " + str(int(0.035 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)

        self.placeholder = QLabel()
        self.placeholder.setFixedWidth(0.02 * self.WINDOW_HEIGHT)
        self.placeholder.setFixedHeight(0.05 * self.WINDOW_HEIGHT)

        self.image_classification = QPushButton(self)
        self.image_classification.setIcon(QIcon(os.path.join(
            'src', 'GUILayout', 'Images', 'Image_classification.png')))
        self.image_classification.setIconSize(QSize(0.3 * self.WINDOW_WIDTH,
                                                    0.3 * self.WINDOW_HEIGHT))
        self.image_classification.setToolTip(
            'Categorize images to different classes.')
        self.image_classification.setStyleSheet(
            """QPushButton {
            font: """ + str(int(0.035 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
            QPushButton::hover {
            background-color : rgb(10, 100, 200)}
            QToolTip {
            font: """ + str(int(0.025 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
            background-color : rgb(53, 53, 53);
            color: white;
            border: black solid 1px}""")
        self.image_classification.setFixedHeight(0.3 * self.WINDOW_HEIGHT)
        self.image_classification.setFixedWidth(0.3 * self.WINDOW_WIDTH)

        self.image_regression = QPushButton(self)
        self.image_regression.setIcon(QIcon(os.path.join(
            'src', 'GUILayout', 'Images', 'Image_regression.png')))
        self.image_regression.setIconSize(QSize(0.3 * self.WINDOW_WIDTH,
                                                0.3 * self.WINDOW_HEIGHT))
        self.image_regression.setToolTip(
            'Images get not categorized, instead you\n'
            'get a value as prediction.')
        self.image_regression.setStyleSheet(
            """QPushButton {
            font: """ + str(int(0.035 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
            QPushButton::hover {
            background-color : rgb(10, 100, 200)}
            QToolTip {
            font: """ + str(int(0.025 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
            background-color : rgb(53, 53, 53);
            color: white;
            border: black solid 1px}""")
        self.image_regression.setFixedHeight(0.3 * self.WINDOW_HEIGHT)
        self.image_regression.setFixedWidth(0.3 * self.WINDOW_WIDTH)

        self.data_classification = QPushButton(self)
        self.data_classification.setIcon(QIcon(os.path.join(
            'src', 'GUILayout', 'Images', 'Data_classification.png')))
        self.data_classification.setIconSize(QSize(0.3 * self.WINDOW_WIDTH,
                                                   0.3 * self.WINDOW_HEIGHT))
        self.data_classification.setToolTip(
            'Categorize data to different classes.')
        self.data_classification.setStyleSheet(
            """QPushButton {
            font: """ + str(int(0.035 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
            QPushButton::hover {
            background-color : rgb(10, 100, 200)}
            QToolTip {
            font: """ + str(int(0.025 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
            background-color : rgb(53, 53, 53);
            color: white;
            border: black solid 1px}""")
        self.data_classification.setFixedHeight(0.3 * self.WINDOW_HEIGHT)
        self.data_classification.setFixedWidth(0.3 * self.WINDOW_WIDTH)

        self.data_regression = QPushButton(self)
        self.data_regression.setIcon(QIcon(os.path.join(
            'src', 'GUILayout', 'Images', 'Data_regression.png')))
        self.data_regression.setIconSize(QSize(0.3 * self.WINDOW_WIDTH,
                                               0.3 * self.WINDOW_HEIGHT))
        self.data_regression.setToolTip(
            'Data get not categorized, instead you\n'
            'get a value as prediction.')
        self.data_regression.setStyleSheet(
            """QPushButton {
            font: """ + str(int(0.035 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
            QPushButton::hover {
            background-color : rgb(10, 100, 200)}
            QToolTip {
            font: """ + str(int(0.025 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
            background-color : rgb(53, 53, 53);
            color: white;
            border: black solid 1px}""")
        self.data_regression.setFixedHeight(0.3 * self.WINDOW_HEIGHT)
        self.data_regression.setFixedWidth(0.3 * self.WINDOW_WIDTH)

        self.step = QLabel(self)
        self.step.setFixedHeight(0.05 * self.WINDOW_HEIGHT)
        step_img = QPixmap(os.path.join(
            'src', 'GUILayout', 'Images', 'GUI_progress_bar',
            'GUI_train_step_3.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)

        self.back = QPushButton(self)
        self.back.setIcon(QIcon(os.path.join(
            'src', 'GUILayout', 'Images', 'back_arrow.png')))
        self.back.setIconSize(QSize(0.04 * self.WINDOW_HEIGHT,
                                    0.04 * self.WINDOW_HEIGHT))
        self.back.setFixedHeight(0.05 * self.WINDOW_HEIGHT)

        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].addStretch()
        self.horizontal_box[0].setAlignment(Qt.AlignTop)

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addItem(QSpacerItem(
            0.1 * self.WINDOW_WIDTH, 0.1 * self.WINDOW_HEIGHT))

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addStretch()
        self.horizontal_box[2].addWidget(self.image_classification)
        self.horizontal_box[2].addStretch()
        self.horizontal_box[2].addWidget(self.image_regression)
        self.horizontal_box[2].addStretch()

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addItem(QSpacerItem(
            0.1 * self.WINDOW_WIDTH, 0.1 * self.WINDOW_HEIGHT))

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[4].addStretch()
        self.horizontal_box[4].addWidget(self.data_classification)
        self.horizontal_box[4].addStretch()
        self.horizontal_box[4].addWidget(self.data_regression)
        self.horizontal_box[4].addStretch()

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[5].addItem(QSpacerItem(
            0.15 * self.WINDOW_WIDTH, 0.15 * self.WINDOW_HEIGHT))

        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.back, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.step, 0, 1, Qt.AlignCenter)
        sublayout.addWidget(self.placeholder, 0, 2, Qt.AlignRight)
        self.horizontal_box[6].addLayout(sublayout)
        self.horizontal_box[6].setAlignment(Qt.AlignBottom)

        self.vertical_box = QVBoxLayout()
        for i in range(0, len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])

        self.setLayout(self.vertical_box)
