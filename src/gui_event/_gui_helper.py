'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

import os
import pandas as pd

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def get_output_path(self, cur_window_label):
    """Get the path where the genareted Project should be stored

    A Browse window opens and you can navigate to the directory
    you wanna store the project.

    Args:
        cur_window_label: Label of GUI window to set a new text.
    """
    self.output_path = QFileDialog.getExistingDirectory(
        self, "Select the output path", os.path.expanduser('~'))
    self.set_label(cur_window_label, self.output_path, Qt.AlignCenter)


def get_model_path(self, cur_window_label):
    """Get the keras model which should be converted

    A Browse window opens and you can navigate to the TensorFlow
    model file you wanna convert to TensorFlow lite.

    Args:
        cur_window_label: Label of GUI window to set a new text.
    """
    self.model_path = QFileDialog.getOpenFileName(self, "Select your model",
                                                  os.path.expanduser('~'))[0]
    self.set_label(cur_window_label, self.model_path, Qt.AlignCenter)


def get_data_loader(self, cur_window, cur_window_label):
    """Get the file or path to load your training data.

    A Browse window opens and you can navigate to the directory
    containing your training data. Otherwise you can select a file
    which loads your training. If the file is a CSV the
    csv_dataloader() function is executed.

    Args:
        cur_window:       GUI window from which the function is executed.
        cur_window_label: Label of GUI window to set a new text.
    """
    if "Select PATH with data" in cur_window.dataloader_list.currentText():
        self.data_loader_path = QFileDialog.getExistingDirectory(
            self, "Select your training data path", os.path.expanduser('~'))
    elif ("Select FILE with data" in
            cur_window.dataloader_list.currentText()):
        self.data_loader_path = QFileDialog.getOpenFileName(
            self, "Select your data loader script", os.path.expanduser('~'),
            'CSV(*.csv);; Python(*.py)')[0]

    if ".csv" in self.data_loader_path:
        print("CSV file selected")
        self.csv_dataloader(cur_window)
    else:
        print("No CSV file")
        self.set_label(cur_window_label, self.data_loader_path, Qt.AlignCenter)


def set_label(self, cur_window_label, label_text, label_alignment):
    """Set a label with a given text

    Args:
        cur_window_label:    Label of GUI window to set a new text.
        label_text:         Text to be inserted in label.
        label_alignment:    Alignment of the label if it is not to long.
    """
    cur_window_label.setText(label_text)
    if (cur_window_label.fontMetrics().boundingRect(
            cur_window_label.text()).width() >
            cur_window_label.width()):
        cur_window_label.setAlignment(Qt.AlignRight)
    else:
        cur_window_label.setAlignment(label_alignment)


def set_pruning(self, cur_window):
    """Adds or removes pruning from optimization.

    If "self.optimizations" doesn't contain pruning it gets added.
    Otherwise it gets removed. Furthermore the input fields for the
    pruning factors appear or disappear.

    Args:
        cur_window: GUI window from which the function is executed.
    """
    if cur_window.pruning.isChecked():
        if "Pruning" not in self.optimizations:
            self.optimizations.append("Pruning")
            print("Optimizations:", self.optimizations)

        cur_window.prun_fac.setVisible(True)
        cur_window.prun_acc.setVisible(True)

        if self.prun_type is not None:
            set_prun_type(self, self.prun_type, cur_window, True)

    else:
        if "Pruning" in self.optimizations:
            self.optimizations.remove("Pruning")
            print("Optimizations:", self.optimizations)
        cur_window.prun_fac.setVisible(False)
        cur_window.prun_acc.setVisible(False)

        cur_window.pruning_dense.setVisible(False)
        cur_window.pruning_conv.setVisible(False)
        cur_window.pruning_conv_label.setVisible(False)
        cur_window.pruning_dense_label.setVisible(False)

        cur_window.min_acc.setVisible(False)
        cur_window.acc_loss.setVisible(False)
        cur_window.prun_acc_label.setVisible(False)
        cur_window.prun_acc_edit.setVisible(False)


def set_quantization(self, cur_window):
    """Adds or removes quantization from optimization.

    If "self.optimizations" doesn't contain quantization it gets added.
    Otherwise it gets removed. Furthermore the buttons for the
    quantization type appear or disappear.

    Args:
        cur_window: GUI window from which the function is executed.
    """
    if cur_window.quantization.isChecked():
        if "Quantization" not in self.optimizations:
            self.optimizations.append("Quantization")
        if self.quant_dtype is not None:
            if "int8 with float fallback" in self.quant_dtype:
                cur_window.quant_int_only.setChecked(False)
                cur_window.quant_int.setChecked(True)
            elif "int8 only" in self.quant_dtype:
                cur_window.quant_int_only.setChecked(True)
                cur_window.quant_int.setChecked(False)
        cur_window.quant_int.setVisible(True)
        cur_window.quant_int_only.setVisible(True)

    else:
        if "Quantization" in self.optimizations:
            self.optimizations.remove("Quantization")
        cur_window.quant_int.setChecked(False)
        cur_window.quant_int_only.setChecked(False)
        cur_window.quant_int.setVisible(False)
        cur_window.quant_int_only.setVisible(False)

    print("Optimizations:", self.optimizations)


def set_prun_type(self, prun_type, cur_window, Pruning_button):
    """Sets the pruning type.

    Checks which button of the pruning type is pressed and
    sets it as pruning type.

    Args:
        prun_type:      Defines the pruning type.
        cur_window:      GUI window from which the function is executed.
        Pruning_button: Was the Pruning button pressed or not
    """
    if "Factor" in prun_type:
        cur_window.prun_acc.setChecked(False)
        cur_window.min_acc.setChecked(False)
        cur_window.acc_loss.setChecked(False)
        if (self.prun_type is None or "Factor" not in self.prun_type or
                Pruning_button):
            cur_window.prun_fac.setChecked(True)
            self.prun_type = prun_type
            self.prun_acc_type = None
            if (self.prun_factor_dense is None and
                    self.prun_factor_conv is None):
                cur_window.pruning_dense.setText("10")
                cur_window.pruning_conv.setText("10")
            else:
                cur_window.pruning_dense.setText(str(self.prun_factor_dense))
                cur_window.pruning_conv.setText(str(self.prun_factor_conv))
            cur_window.pruning_dense.setVisible(True)
            cur_window.pruning_conv.setVisible(True)
            cur_window.pruning_conv_label.setVisible(True)
            cur_window.pruning_dense_label.setVisible(True)

            cur_window.min_acc.setVisible(False)
            cur_window.acc_loss.setVisible(False)
            cur_window.prun_acc_label.setVisible(False)
            cur_window.prun_acc_edit.setVisible(False)
        else:
            self.prun_type = None
            cur_window.pruning_dense.setVisible(False)
            cur_window.pruning_conv.setVisible(False)
            cur_window.pruning_conv_label.setVisible(False)
            cur_window.pruning_dense_label.setVisible(False)

    elif "Accuracy" in prun_type:
        cur_window.prun_fac.setChecked(False)
        if (self.prun_type is None or "Accuracy" not in self.prun_type or
                Pruning_button):
            cur_window.prun_acc.setChecked(True)
            self.prun_type = prun_type

            cur_window.min_acc.setVisible(True)
            cur_window.acc_loss.setVisible(True)

            print("Accuracy pruning type:", self.prun_acc_type)
            if (self.prun_acc_type is not None and
                    "Minimal accuracy" in self.prun_acc_type):
                cur_window.min_acc.setChecked(True)
                cur_window.acc_loss.setChecked(False)
                cur_window.prun_acc_label.setText("Min accuracy\n"
                                                  "to reach in %")
                cur_window.prun_acc_label.setVisible(True)
                cur_window.prun_acc_edit.setVisible(True)
                if self.prun_acc is None:
                    cur_window.prun_acc_edit.setText("90")
                else:
                    cur_window.prun_acc_edit.setText(str(self.prun_acc))

            elif (self.prun_acc_type is not None and
                    "Accuracy loss" in self.prun_acc_type):
                cur_window.min_acc.setChecked(False)
                cur_window.acc_loss.setChecked(True)
                cur_window.prun_acc_label.setText("Max accuracy\nloss in %")
                cur_window.prun_acc_label.setVisible(True)
                cur_window.prun_acc_edit.setVisible(True)
                if self.prun_acc is None:
                    cur_window.prun_acc_edit.setText("3")
                else:
                    cur_window.prun_acc_edit.setText(str(self.prun_acc))

            try:
                self.prun_factor_dense = int(cur_window.pruning_dense.text())
                self.prun_factor_conv = int(cur_window.pruning_conv.text())
            except:
                self.prun_factor_dense = None
                self.prun_factor_conv = None
            cur_window.pruning_dense.setVisible(False)
            cur_window.pruning_conv.setVisible(False)
            cur_window.pruning_conv_label.setVisible(False)
            cur_window.pruning_dense_label.setVisible(False)
        else:
            self.prun_type = None
            self.prun_acc_type = None
            cur_window.min_acc.setChecked(False)
            cur_window.acc_loss.setChecked(False)

            cur_window.min_acc.setVisible(False)
            cur_window.acc_loss.setVisible(False)
            cur_window.prun_acc_label.setVisible(False)
            cur_window.prun_acc_edit.setVisible(False)
    print("Pruning type:", self.prun_type)


def set_prun_acc_type(self, prun_type, cur_window):
    """Sets the pruning for accuracy type.

    Sets and unsets the checked pruning for accuracy type.

    Args:
        prun_acc_type: Defines the pruning for accuracy type.
        cur_window:     GUI window from which the function is executed.
    """
    if "Minimal accuracy" in prun_type:
        cur_window.acc_loss.setChecked(False)
        if (self.prun_acc_type is None or
                "Minimal accuracy" not in self.prun_acc_type):
            self.prun_acc_type = prun_type
            cur_window.prun_acc_label.setVisible(True)
            cur_window.prun_acc_label.setText("Min accuracy\nto reach in %")
            cur_window.prun_acc_edit.setVisible(True)
            cur_window.prun_acc_edit.setText("90")
            self.prun_acc = None
        else:
            self.prun_acc_type = None
            cur_window.prun_acc_label.setVisible(False)
            cur_window.prun_acc_edit.setVisible(False)
    elif "Accuracy loss" in prun_type:
        cur_window.min_acc.setChecked(False)
        if (self.prun_acc_type is None or
                "Accuracy loss" not in self.prun_acc_type):
            self.prun_acc_type = prun_type
            cur_window.prun_acc_label.setVisible(True)
            cur_window.prun_acc_label.setText("Max accuracy\nloss in %")
            cur_window.prun_acc_edit.setVisible(True)
            cur_window.prun_acc_edit.setText("3")
            self.prun_acc = None
        else:
            self.prun_acc_type = None
            cur_window.prun_acc_label.setVisible(False)
            cur_window.prun_acc_edit.setVisible(False)
    print("Accuracy pruning type:", self.prun_acc_type)


def set_quant_dtype(self, dtype, cur_window):
    """Sets the quantization type.

    Checks which button of the quantization type is pressed and
    sets it as quantization type.

    Args:
        dtype:     Defines the quantization type.
        cur_window: GUI window from which the function is executed.
    """
    if "int8 with float fallback" in dtype:
        cur_window.quant_int_only.setChecked(False)
        if not cur_window.quant_int.isChecked():
            self.quant_dtype = None
        else:
            self.quant_dtype = dtype
    elif "int8 only" in dtype:
        cur_window.quant_int.setChecked(False)
        if not cur_window.quant_int_only.isChecked():
            self.quant_dtype = None
        else:
            self.quant_dtype = dtype
    print("Quantization type:", self.quant_dtype)


def model_pruning(self, cur_window):
    """Starts the thread to prune the model.

    The thread for pruning the model is started. Also, the two
    buttons of the GUI window are hidden and the thread for the
    loading screen is started.

    Args:
        cur_window: GUI window from which the function is executed.
    """
    cur_window.model_memory_label.setVisible(False)
    cur_window.model_memory.setVisible(False)
    cur_window.model_memory_label_kb.setVisible(False)
    cur_window.summary.setVisible(False)
    cur_window.project_name_label.setVisible(False)
    cur_window.project_name_label_2.setVisible(False)
    cur_window.output_path_label.setVisible(False)
    cur_window.output_path_label_2.setVisible(False)
    cur_window.model_path_label.setVisible(False)
    cur_window.model_path_label_2.setVisible(False)
    cur_window.target_label.setVisible(False)
    cur_window.target_label_2.setVisible(False)
    cur_window.optimizations_label.setVisible(False)
    cur_window.optimizations_label_2.setVisible(False)
    cur_window.pruning_label.setVisible(False)
    cur_window.pruning_label_2.setVisible(False)
    cur_window.quantization_label.setVisible(False)
    cur_window.quantization_label_2.setVisible(False)
    cur_window.data_loader_label.setVisible(False)
    cur_window.data_loader_label_2.setVisible(False)

    cur_window.back.setVisible(False)
    cur_window.load.setVisible(False)
    cur_window.back_load_placeholder.setVisible(True)
    cur_window.back_load_placeholder.setVisible(True)

    cur_window.load_png.setVisible(True)

    cur_window.loading_images.start()
    cur_window.prune_model.start()


def convert_create(self, cur_window):
    """Starts the thread to convert the model and create the project.

    The thread for pruning the model gets terminated and the thread
    to convert the model and create the project gets started.

    Args:
        cur_window: GUI window from which the function is executed.
    """
    try:
        cur_window.prune_model.stop_thread()
        if "MCU" in self.target:
            cur_window.conv_build_load.set_model_memory(self.model_memory)
        cur_window.conv_build_load.start()
    except:
        print("Error")


def terminate_thread(self, cur_window):
    """End of converting the model and creating the project.

    Terminates the threads for pruning the model and converting the
    model and creating the project. Additionally, the "Finish" button
    becomes visible to close the GUI and the image of the loading
    screen signals the end of the process.

    Args:
        cur_window: GUI window from which the function is executed.
    """
    try:
        print("Finish!")
        cur_window.loading_images.stop_thread()
        cur_window.conv_build_load.stop_thread()
        cur_window.finish_placeholder.setVisible(False)
        cur_window.finish.setVisible(True)
        cur_window.load_png.setPixmap(QPixmap(os.path.join(
            "src", "gui_layout", "images", "gui_loading_images",
            "GUI_load_finish.png")))
        cur_window.load_png.setScaledContents(True)
    except:
        print("Error")


def browse_csv_data(self, cur_window):
    """Get the CSV file which contains your data.

    A Browse window opens and you can navigate to the CSV
    file which contains your data.
    """
    self.data_loader_path = QFileDialog.getOpenFileName(
        self, "Select your data loader script", os.path.expanduser('~'),
        'CSV(*.csv)')[0]
    print("CSV data path:", self.data_loader_path)

    cur_window.table.setRowCount(0)
    cur_window.table.setColumnCount(0)
    cur_window.label_col.setVisible(False)
    cur_window.cb_label_col.setVisible(False)
    cur_window.tot_row.setVisible(False)
    cur_window.num_row.setText("")
    cur_window.tot_col.setVisible(False)
    cur_window.num_col.setText("")


def preview_csv_data(self, cur_window):
    """Gives a preview of the CSV data structure.

    Read the CSV file and separate the data according the selected
    separators. The data is represented by a table. Additionally, a
    drop-down list appears where the column of the data label can
    be selected. Also the number of rows and columns of the data get
    displayed.

    Args:
        cur_window: GUI window from which the function is executed.
    """
    try:
        # Change shape of cursor to wait cursor
        QApplication.setOverrideCursor(Qt.WaitCursor)

        if (self.data_loader_path is not None and
                ".csv" in self.data_loader_path):
            self.get_separator(cur_window)
            decimal = cur_window.dec_label_col.currentText()
            if not self.separator:
                df = pd.read_csv(
                    self.data_loader_path, decimal=decimal, index_col=False)
            else:
                df = pd.read_csv(
                    self.data_loader_path, decimal=decimal, index_col=False,
                    sep=self.separator)
            if df.size == 0:
                return
            df.fillna('', inplace=True)
            cur_window.table.setRowCount(df.shape[0])
            cur_window.table.setColumnCount(df.shape[1])
            # returns pandas array object
            for row in df.iterrows():
                values = row[1]
                for col_index, value in enumerate(values):
                    tableItem = QTableWidgetItem(str(value))
                    cur_window.table.setItem(row[0], col_index, tableItem)

            cur_window.label_col.setVisible(True)
            cur_window.cb_label_col.setVisible(True)

            cur_window.tot_row.setVisible(True)
            cur_window.num_row.setText(str(df.shape[0]))
            cur_window.tot_col.setVisible(True)
            cur_window.num_col.setText(str(df.shape[1]))

            # Default cursor shape
            QApplication.restoreOverrideCursor()

        else:
            # Default cursor shape
            QApplication.restoreOverrideCursor()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)

            msg.setText("Preview of data failed.")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()

    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText("This separator cannot be used")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()


def load_csv_data(self, cur_window, MainWindow):
    """Stores the target column of the CSV file and closes the window.
    """
    if cur_window.cb_label_col.isVisible():
        self.csv_target_label = cur_window.cb_label_col.currentText()
        self.decimal = cur_window.dec_label_col.currentText()
        cur_window.close()
        self.set_label(MainWindow.data_path_label, self.data_loader_path,
                       Qt.AlignCenter)
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)

        msg.setText("You have to preview the data before you can load it.")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
        return


def get_separator(self, cur_window):
    """Read the selected separators.

    Checks if the different separator check boxes are checked or
    not. If a checkbox is selected, the corresponding separator is
    written to the variable "self.separator".

    Args:
        cur_window: GUI window from which the function is executed.
    """
    self.separator = None

    if cur_window.cb_tab.isChecked():
        if self.separator is None:
            self.separator = r'\t'
        else:
            self.separator += r'|\t'
    if cur_window.cb_semicolon.isChecked():
        if self.separator is None:
            self.separator = ';'
        else:
            self.separator += '|;'
    if cur_window.cb_comma.isChecked():
        if self.separator is None:
            self.separator = ','
        else:
            self.separator += '|,'
    if cur_window.cb_space.isChecked():
        if self.separator is None:
            self.separator = r'\s+'
        else:
            self.separator += r'|\s+'
    if cur_window.cb_other.isChecked():
        if self.separator is None:
            self.separator = cur_window.other_separator.text()
        else:
            self.separator += '|' + cur_window.other_separator.text()

    print("CSV sperator:", self.separator)
