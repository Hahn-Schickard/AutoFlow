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


class UICSVDataloader(QWidget):
    """Get a preview and load CSV data.

    This GUI window shows the data format of CSV files, selected
    from the dataloader. You can also choose how to separate the
    different columns and whats the target column.
    """
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, FONT_STYLE, parent=None):
        super(UICSVDataloader, self).__init__(parent)

        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.FONT_STYLE = FONT_STYLE

        self.setWindowModality(Qt.ApplicationModal)

        self.setFixedSize(0.85 * self.WINDOW_WIDTH, 0.85 * self.WINDOW_HEIGHT)
        self.setWindowTitle('CSV dataloader')
        self.setWindowIcon(QIcon(os.path.join(
            "src", "gui_layout", "images", "Window_Icon_blue.png")))

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table = QTableWidget()
        self.table.setFixedHeight(0.4 * self.WINDOW_HEIGHT)
        self.table.setStyleSheet(
            "font: " + str(int(0.025 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        layout.addWidget(self.table)

        self.browse = QPushButton('Browse...')
        self.browse.setFixedWidth(0.2 * self.WINDOW_WIDTH)
        self.browse.setFixedHeight(0.05 * self.WINDOW_HEIGHT)
        self.browse.setToolTip('Select a CSV file.')
        self.browse.setStyleSheet(
            """QPushButton {
            font: """ + str(int(0.035 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
            QPushButton::hover {
            background-color : rgb(10, 100, 200)}
            QToolTip {
            font: """ + str(int(0.025 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
            background-color : rgb(53, 53, 53);
            color: white;
            border: black solid 1px}""")

        self.preview = QPushButton('Preview')
        self.preview.setFixedWidth(0.2 * self.WINDOW_WIDTH)
        self.preview.setFixedHeight(0.05 * self.WINDOW_HEIGHT)
        self.preview.setToolTip(
            'Show an overview of how the data will look with\n'
            'the selected settings, in the table above.')
        self.preview.setStyleSheet(
            """QPushButton {
            font: """ + str(int(0.035 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
            QPushButton::hover {
            background-color : rgb(10, 100, 200)}
            QToolTip {
            font: """ + str(int(0.025 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
            background-color : rgb(53, 53, 53);
            color: white;
            border: black solid 1px}""")

        self.load_data = QPushButton('Load data')
        self.load_data.setFixedWidth(0.2 * self.WINDOW_WIDTH)
        self.load_data.setFixedHeight(0.05 * self.WINDOW_HEIGHT)
        self.load_data.setToolTip(
            'Closes the CSV dataloader window and takes the\n'
            'chosen settings for the later optimization.')
        self.load_data.setStyleSheet(
            """QPushButton {
            font: """ + str(int(0.035 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """}
            QPushButton::hover {
            background-color : rgb(10, 100, 200)}
            QToolTip {
            font: """ + str(int(0.025 * self.WINDOW_HEIGHT)) + """px """ + FONT_STYLE + """;
            background-color : rgb(53, 53, 53);
            color: white;
            border: black solid 1px}""")

        sublayout = QHBoxLayout()
        sublayout.addWidget(self.browse)
        sublayout.addWidget(self.preview)
        sublayout.addWidget(self.load_data)
        layout.addLayout(sublayout)

        self.separator = QLabel("Separator:")
        self.separator.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.separator.setFixedWidth(0.25 * self.WINDOW_WIDTH)
        self.separator.setFixedHeight(0.04 * self.WINDOW_HEIGHT)
        layout.addWidget(self.separator)

        self.cb_tab = QCheckBox('Tab stop', self)
        self.cb_tab.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.cb_tab.setFixedWidth(0.2 * self.WINDOW_WIDTH)
        self.cb_tab.setFixedHeight(0.04 * self.WINDOW_HEIGHT)

        self.label_dec = QLabel("Decimal:")
        self.label_dec.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.label_dec.setFixedWidth(0.16 * self.WINDOW_WIDTH)
        self.label_dec.setFixedHeight(0.04 * self.WINDOW_HEIGHT)

        self.dec_label_col = QComboBox()
        self.dec_label_col.setStyleSheet(
            "font: " + str(int(0.03 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.dec_label_col.setFixedWidth(0.1 * self.WINDOW_WIDTH)
        self.dec_label_col.setFixedHeight(0.04 * self.WINDOW_HEIGHT)
        self.dec_label_col.addItems([".", ","])

        sublayout2 = QHBoxLayout()
        sublayout2.addWidget(self.cb_tab)
        sublayout2.addStretch()
        sublayout2.addWidget(self.label_dec)
        sublayout2.addWidget(self.dec_label_col)
        sublayout2.addItem(QSpacerItem(
            0.201 * self.WINDOW_WIDTH, 0.04 * self.WINDOW_HEIGHT))
        sublayout2.addStretch()
        layout.addLayout(sublayout2)

        self.cb_semicolon = QCheckBox('Semicolon', self)
        self.cb_semicolon.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.cb_semicolon.setFixedWidth(0.2 * self.WINDOW_WIDTH)
        self.cb_semicolon.setFixedHeight(0.04 * self.WINDOW_HEIGHT)

        self.label_col = QLabel("Label column:")
        self.label_col.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.label_col.setFixedWidth(0.16 * self.WINDOW_WIDTH)
        self.label_col.setFixedHeight(0.04 * self.WINDOW_HEIGHT)
        self.label_col.setVisible(False)

        self.cb_label_col = QComboBox()
        self.cb_label_col.setStyleSheet(
            "font: " + str(int(0.03 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.cb_label_col.setFixedWidth(0.1 * self.WINDOW_WIDTH)
        self.cb_label_col.setFixedHeight(0.04 * self.WINDOW_HEIGHT)
        self.cb_label_col.addItems(["First", "Last"])
        self.cb_label_col.setVisible(False)

        sublayout3 = QHBoxLayout()
        sublayout3.addWidget(self.cb_semicolon)
        sublayout3.addStretch()
        sublayout3.addWidget(self.label_col)
        sublayout3.addWidget(self.cb_label_col)
        sublayout3.addItem(QSpacerItem(
            0.201 * self.WINDOW_WIDTH, 0.04 * self.WINDOW_HEIGHT))
        sublayout3.addStretch()
        layout.addLayout(sublayout3)

        self.cb_comma = QCheckBox('Comma', self)
        self.cb_comma.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.cb_comma.setFixedWidth(0.2 * self.WINDOW_WIDTH)
        self.cb_comma.setFixedHeight(0.04 * self.WINDOW_HEIGHT)

        self.tot_row = QLabel('Total rows:', self)
        self.tot_row.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.tot_row.setFixedWidth(0.16 * self.WINDOW_WIDTH)
        self.tot_row.setFixedHeight(0.04 * self.WINDOW_HEIGHT)
        self.tot_row.setAlignment(Qt.AlignLeft)
        self.tot_row.setVisible(False)

        self.num_row = QLabel()
        self.num_row.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.num_row.setFixedWidth(0.3 * self.WINDOW_WIDTH)
        self.num_row.setFixedHeight(0.04 * self.WINDOW_HEIGHT)
        self.num_row.setAlignment(Qt.AlignLeft)

        sublayout4 = QHBoxLayout()
        sublayout4.addWidget(self.cb_comma)
        sublayout4.addStretch()
        sublayout4.addWidget(self.tot_row)
        sublayout4.addWidget(self.num_row)
        sublayout4.addStretch()
        layout.addLayout(sublayout4)

        self.cb_space = QCheckBox('Space', self)
        self.cb_space.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.cb_space.setFixedWidth(0.2 * self.WINDOW_WIDTH)
        self.cb_space.setFixedHeight(0.04 * self.WINDOW_HEIGHT)

        self.tot_col = QLabel('Total columns:', self)
        self.tot_col.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.tot_col.setFixedWidth(0.16 * self.WINDOW_WIDTH)
        self.tot_col.setFixedHeight(0.04 * self.WINDOW_HEIGHT)
        self.tot_col.setAlignment(Qt.AlignLeft)
        self.tot_col.setVisible(False)

        self.num_col = QLabel()
        self.num_col.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.num_col.setFixedWidth(0.3 * self.WINDOW_WIDTH)
        self.num_col.setFixedHeight(0.04 * self.WINDOW_HEIGHT)
        self.num_col.setAlignment(Qt.AlignLeft)

        sublayout5 = QHBoxLayout()
        sublayout5.addWidget(self.cb_space)
        sublayout5.addStretch()
        sublayout5.addWidget(self.tot_col)
        sublayout5.addWidget(self.num_col)
        sublayout5.addStretch()
        layout.addLayout(sublayout5)

        self.cb_other = QCheckBox('other', self)
        self.cb_other.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)
        self.cb_other.setFixedWidth(0.095 * self.WINDOW_WIDTH)
        self.cb_other.setFixedHeight(0.04 * self.WINDOW_HEIGHT)

        self.other_separator = QLineEdit()
        self.other_separator.setFixedWidth(0.05 * self.WINDOW_WIDTH)
        self.other_separator.setFixedHeight(0.04 * self.WINDOW_HEIGHT)
        self.other_separator.setMaxLength(1)
        self.other_separator.setStyleSheet(
            "font: " + str(int(0.032 * self.WINDOW_HEIGHT)) + "px " +
            FONT_STYLE)

        sublayout6 = QHBoxLayout()
        sublayout6.addWidget(self.cb_other)
        sublayout6.addWidget(self.other_separator)
        sublayout6.addStretch()
        layout.addLayout(sublayout6)
