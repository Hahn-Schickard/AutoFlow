''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class UICSVDataloaderWindow(QWidget):
    """Get a preview and load CSV data. 

    This GUI window shows the data format of CSV files, selected
    from the dataloader. You can also choose how to separate the 
    different columns and whats the target column.
    """
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, parent=None):
        super(UICSVDataloaderWindow, self).__init__(parent)

        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE

        self.setWindowModality(Qt.ApplicationModal)

        self.setFixedSize(0.85*self.WINDOW_WIDTH, 0.85*self.WINDOW_HEIGHT)
        self.setWindowTitle('CSV dataloader')
        self.setWindowIcon(QIcon(os.path.join("Images", "Window_Icon_blue.png"))) 

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table = QTableWidget()
        self.table.setFixedHeight(0.4*self.WINDOW_HEIGHT)
        self.table.setStyleSheet("font: " + str(int(0.025*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        layout.addWidget(self.table)

        self.Browse = QPushButton('Browse...')
        self.Browse.setFixedWidth(0.2*self.WINDOW_WIDTH)
        self.Browse.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.Browse.setToolTip('Select a CSV file')
        self.Browse.setStyleSheet("""QPushButton {
                           font: """ + str(int(0.035*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""") 

        self.Preview = QPushButton('Preview')
        self.Preview.setFixedWidth(0.2*self.WINDOW_WIDTH)
        self.Preview.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.Preview.setToolTip('Show an overview of how the data will look with\n'
                                'the selected settings, in the table above.')
        self.Preview.setStyleSheet("""QPushButton {
                           font: """ + str(int(0.035*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""") 

        self.Load_data = QPushButton('Load data')
        self.Load_data.setFixedWidth(0.2*self.WINDOW_WIDTH)
        self.Load_data.setFixedHeight(0.05*self.WINDOW_HEIGHT)
        self.Load_data.setToolTip('Closes the CSV dataloader window and takes the\n'
                                  'chosen settings for the later optimization.')
        self.Load_data.setStyleSheet("""QPushButton {
                           font: """ + str(int(0.035*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
                           QPushButton::hover {
                           background-color : rgb(10, 100, 200)}
                           QToolTip { 
                           font: """ + str(int(0.025*self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
                           background-color : rgb(53, 53, 53);
                           color: white; 
                           border: black solid 1px}""") 

        sublayout = QHBoxLayout()
        sublayout.addWidget(self.Browse)
        sublayout.addWidget(self.Preview)
        sublayout.addWidget(self.Load_data)
        layout.addLayout(sublayout)

        self.separator = QLabel("Separator:")
        self.separator.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.separator.setFixedWidth(0.25*self.WINDOW_WIDTH)
        self.separator.setFixedHeight(0.04*self.WINDOW_HEIGHT)
        layout.addWidget(self.separator)

        self.cbTab = QCheckBox('Tab stop', self)
        self.cbTab.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.cbTab.setFixedWidth(0.2*self.WINDOW_WIDTH)
        self.cbTab.setFixedHeight(0.04*self.WINDOW_HEIGHT)
        layout.addWidget(self.cbTab)

        self.cbSemicolon = QCheckBox('Semicolon', self)
        self.cbSemicolon.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.cbSemicolon.setFixedWidth(0.2*self.WINDOW_WIDTH)
        self.cbSemicolon.setFixedHeight(0.04*self.WINDOW_HEIGHT)

        self.label_col = QLabel("Label column:")
        self.label_col.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.label_col.setFixedWidth(0.16*self.WINDOW_WIDTH)
        self.label_col.setFixedHeight(0.04*self.WINDOW_HEIGHT)
        self.label_col.setVisible(False)
        
        self.cb_label_col = QComboBox()
        self.cb_label_col.setStyleSheet("font: " + str(int(0.03*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.cb_label_col.setFixedWidth(0.1*self.WINDOW_WIDTH)
        self.cb_label_col.setFixedHeight(0.04*self.WINDOW_HEIGHT)
        self.cb_label_col.addItems(["First", "Last"])
        self.cb_label_col.setVisible(False)

        sublayout2 = QHBoxLayout()
        sublayout2.addWidget(self.cbSemicolon)
        sublayout2.addStretch()
        sublayout2.addWidget(self.label_col)
        sublayout2.addWidget(self.cb_label_col)
        sublayout2.addItem(QSpacerItem(0.201*self.WINDOW_WIDTH, 0.04*self.WINDOW_HEIGHT))
        sublayout2.addStretch()
        layout.addLayout(sublayout2)

        self.cbComma = QCheckBox('Comma', self)
        self.cbComma.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.cbComma.setFixedWidth(0.2*self.WINDOW_WIDTH)
        self.cbComma.setFixedHeight(0.04*self.WINDOW_HEIGHT)

        self.totRow = QLabel('Total rows:', self)
        self.totRow.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.totRow.setFixedWidth(0.16*self.WINDOW_WIDTH)
        self.totRow.setFixedHeight(0.04*self.WINDOW_HEIGHT)
        self.totRow.setAlignment(Qt.AlignLeft)
        self.totRow.setVisible(False)

        self.numRow = QLabel()
        self.numRow.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.numRow.setFixedWidth(0.3*self.WINDOW_WIDTH)
        self.numRow.setFixedHeight(0.04*self.WINDOW_HEIGHT)
        self.numRow.setAlignment(Qt.AlignLeft)

        sublayout3 = QHBoxLayout()
        sublayout3.addWidget(self.cbComma)
        sublayout3.addStretch()
        sublayout3.addWidget(self.totRow)
        sublayout3.addWidget(self.numRow)
        sublayout3.addStretch()
        layout.addLayout(sublayout3)

        self.cbSpace = QCheckBox('Space', self)
        self.cbSpace.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.cbSpace.setFixedWidth(0.2*self.WINDOW_WIDTH)
        self.cbSpace.setFixedHeight(0.04*self.WINDOW_HEIGHT)

        self.totCol = QLabel('Total columns:', self)
        self.totCol.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.totCol.setFixedWidth(0.16*self.WINDOW_WIDTH)
        self.totCol.setFixedHeight(0.04*self.WINDOW_HEIGHT)
        self.totCol.setAlignment(Qt.AlignLeft)
        self.totCol.setVisible (False)

        self.numCol = QLabel()
        self.numCol.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.numCol.setFixedWidth(0.3*self.WINDOW_WIDTH)
        self.numCol.setFixedHeight(0.04*self.WINDOW_HEIGHT)
        self.numCol.setAlignment(Qt.AlignLeft)

        sublayout4 = QHBoxLayout()
        sublayout4.addWidget(self.cbSpace)
        sublayout4.addStretch()
        sublayout4.addWidget(self.totCol)
        sublayout4.addWidget(self.numCol)
        sublayout4.addStretch()
        layout.addLayout(sublayout4)

        self.cbOther = QCheckBox('other', self)
        self.cbOther.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)
        self.cbOther.setFixedWidth(0.095*self.WINDOW_WIDTH)
        self.cbOther.setFixedHeight(0.04*self.WINDOW_HEIGHT)

        self.other_separator = QLineEdit()
        self.other_separator.setFixedWidth(0.05*self.WINDOW_WIDTH)
        self.other_separator.setFixedHeight(0.04*self.WINDOW_HEIGHT)
        self.other_separator.setMaxLength(1)
        self.other_separator.setStyleSheet("font: " + str(int(0.032*self.WINDOW_HEIGHT)) + "px " + FONT_STYLE)

        sublayout5 = QHBoxLayout()
        sublayout5.addWidget(self.cbOther)
        sublayout5.addWidget(self.other_separator)
        sublayout5.addStretch()
        layout.addLayout(sublayout5)