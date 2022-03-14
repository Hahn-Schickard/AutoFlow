'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: GPL-3.0
============================================================================'''

import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UITargetPlatform(QWidget):
    """Select the target where the neural network should
    be executed.

    In this window you can choose on which device the neural network
    should be executed. You can choose if you want to execute it on
    an MCU, FPGA or SBC.
    """
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, parent=None):
        super(UITargetPlatform, self).__init__(parent)

        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE

        self.label = QLabel("Choose your target")
        self.label.setStyleSheet(
            "font: " + str(int(0.035 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.label.setAlignment(Qt.AlignCenter)

        self.mcu = QPushButton(self)
        self.mcu.setIcon(QIcon(os.path.join(
            'src', 'gui_layout', 'images', 'MCU.png')))
        self.mcu.setIconSize(QSize(0.2 * self.WINDOW_WIDTH,
                                   0.25 * self.WINDOW_HEIGHT))
        self.mcu.setToolTip('Run the TensorFlow model on an MCU.')
        self.mcu.setStyleSheet(
            """QPushButton {
            font: """ + str(int(0.035 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
            QPushButton::hover {
            background-color : rgb(10, 100, 200)}
            QToolTip {
            font: """ + str(int(0.025 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
            background-color : rgb(53, 53, 53);
            color: white;
            border: black solid 1px}""")
        self.mcu.setFixedHeight(0.3 * self.WINDOW_HEIGHT)
        self.mcu.setFixedWidth(0.3 * self.WINDOW_WIDTH)

        self.fpga = QPushButton(self)
        self.fpga.setIcon(QIcon(os.path.join(
            'src', 'gui_layout', 'images', 'FPGA.png')))
        self.fpga.setIconSize(QSize(0.2 * self.WINDOW_WIDTH,
                                    0.25 * self.WINDOW_HEIGHT))
        self.fpga.setToolTip('Run the TensorFlow model on an FPGA.')
        self.fpga.setStyleSheet(
            """QPushButton {
            font: """ + str(int(0.035 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
            QPushButton::hover {
            background-color : rgb(10, 100, 200)}
            QToolTip {
            font: """ + str(int(0.025 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
            background-color : rgb(53, 53, 53);
            color: white;
            border: black solid 1px}""")
        self.fpga.setFixedHeight(0.3 * self.WINDOW_HEIGHT)
        self.fpga.setFixedWidth(0.3 * self.WINDOW_WIDTH)

        self.sbc = QPushButton(self)
        self.sbc.setIcon(QIcon(os.path.join(
            'src', 'gui_layout', 'images', 'sbc.png')))
        self.sbc.setIconSize(QSize(0.25 * self.WINDOW_WIDTH,
                                   0.25 * self.WINDOW_HEIGHT))
        self.sbc.setToolTip('Run the TensorFlow model on an SBC.')
        self.sbc.setStyleSheet(
            """QPushButton {
            font: """ + str(int(0.035 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
            QPushButton::hover {
            background-color : rgb(10, 100, 200)}
            QToolTip {
            font: """ + str(int(0.025 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
            background-color : rgb(53, 53, 53);
            color: white;
            border: black solid 1px}""")
        self.sbc.setFixedHeight(0.3 * self.WINDOW_HEIGHT)
        self.sbc.setFixedWidth(0.3 * self.WINDOW_WIDTH)

        self.back = QPushButton(self)
        self.back.setIcon(QIcon(os.path.join(
            'src', 'gui_layout', 'images', 'back_arrow.png')))
        self.back.setIconSize(QSize(0.04 * self.WINDOW_HEIGHT,
                                    0.04 * self.WINDOW_HEIGHT))
        self.back.setFixedHeight(0.05 * self.WINDOW_HEIGHT)

        self.step = QLabel(self)
        self.step.setFixedHeight(0.05 * self.WINDOW_HEIGHT)
        step_img = QPixmap(os.path.join(
            'src', 'gui_layout', 'images', 'gui_progress_bar',
            'GUI_load_step_3.png'))
        self.step.setPixmap(step_img)
        self.step.setAlignment(Qt.AlignCenter)

        self.placeholder_button = QLabel()
        self.placeholder_button.setFixedHeight(0.05 * self.WINDOW_HEIGHT)

        self.horizontal_box = []
        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[0].addWidget(self.label)
        self.horizontal_box[0].setAlignment(Qt.AlignTop)

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[1].addItem(QSpacerItem(
            self.WINDOW_WIDTH, 0.1 * self.WINDOW_HEIGHT))

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[2].addWidget(self.mcu)
        self.horizontal_box[2].addWidget(self.fpga)
        self.horizontal_box[2].addWidget(self.sbc)

        self.horizontal_box.append(QHBoxLayout())
        self.horizontal_box[3].addItem(QSpacerItem(
            self.WINDOW_WIDTH, 0.3 * self.WINDOW_HEIGHT))

        self.horizontal_box.append(QHBoxLayout())
        sublayout = QGridLayout()
        sublayout.addWidget(self.back, 0, 0, Qt.AlignLeft)
        sublayout.addWidget(self.step, 0, 1, Qt.AlignCenter)
        sublayout.addWidget(self.placeholder_button, 0, 2, Qt.AlignRight)
        self.horizontal_box[4].addLayout(sublayout)

        self.vertical_box = QVBoxLayout()
        for i in range(0, len(self.horizontal_box)):
            self.vertical_box.addLayout(self.horizontal_box[i])

        self.setLayout(self.vertical_box)
