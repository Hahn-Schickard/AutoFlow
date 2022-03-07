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


def get_output_path(self, CurWindow_label):
    """Get the path where the genareted Project should be stored

    A Browse window opens and you can navigate to the directory
    you wanna store the project.

    Args:
        CurWindow_label: Label of GUI window to set a new text.
    """
    self.output_path = QFileDialog.getExistingDirectory(
        self, "Select the output path", os.path.expanduser('~'))
    self.set_label(CurWindow_label, self.output_path, Qt.AlignCenter)


def get_model_path(self, CurWindow_label):
    """Get the keras model which should be converted

    A Browse window opens and you can navigate to the TensorFlow
    model file you wanna convert to TensorFlow lite.

    Args:
        CurWindow_label: Label of GUI window to set a new text.
    """
    self.model_path = QFileDialog.getOpenFileName(self, "Select your model",
                                                  os.path.expanduser('~'))[0]
    self.set_label(CurWindow_label, self.model_path, Qt.AlignCenter)


def get_data_loader(self, CurWindow, CurWindow_label):
    """Get the file or path to load your training data.

    A Browse window opens and you can navigate to the directory
    containing your training data. Otherwise you can select a file
    which loads your training. If the file is a CSV the
    CSVDataloaderWindow() function is executed.

    Args:
        CurWindow:       GUI window from which the function is executed.
        CurWindow_label: Label of GUI window to set a new text.
    """
    if "Select PATH with data" in CurWindow.dataloader_list.currentText():
        self.data_loader_path = QFileDialog.getExistingDirectory(
            self, "Select your trainingdata path", os.path.expanduser('~'))
    elif ("Select FILE with data" in
            CurWindow.dataloader_list.currentText()):
        self.data_loader_path = QFileDialog.getOpenFileName(
            self, "Select your data loader script", os.path.expanduser('~'),
            'CSV(*.csv);; Python(*.py)')[0]

    if ".csv" in self.data_loader_path:
        print("CSV file selected")
        self.CSVDataloaderWindow(CurWindow)
    else:
        print("No CSV file")
        self.set_label(CurWindow_label, self.data_loader_path, Qt.AlignCenter)


def set_label(self, CurWindow_label, label_text, label_alignment):
    """Set a label with a given text

    Args:
        CurWindow_label:    Label of GUI window to set a new text.
        label_text:         Text to be inserted in label.
        label_alignment:    Alignment of the label if it is not to long.
    """
    CurWindow_label.setText(label_text)
    if (CurWindow_label.fontMetrics().boundingRect(
            CurWindow_label.text()).width() >
            CurWindow_label.width()):
        CurWindow_label.setAlignment(Qt.AlignRight)
    else:
        CurWindow_label.setAlignment(label_alignment)


def set_pruning(self, CurWindow):
    """Adds or removes pruning from optimization.

    If "self.optimizations" doesn't contain pruning it gets added.
    Otherwise it gets removed. Furthermore the input fields for the
    pruning factors appear or disappear.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    if CurWindow.pruning.isChecked():
        if "Pruning" not in self.optimizations:
            self.optimizations.append("Pruning")
            print("Optimizations:", self.optimizations)

        CurWindow.prun_fac.setVisible(True)
        CurWindow.prun_acc.setVisible(True)

        if self.prun_type is not None:
            set_prun_type(self, self.prun_type, CurWindow, True)

    else:
        if "Pruning" in self.optimizations:
            self.optimizations.remove("Pruning")
            print("Optimizations:", self.optimizations)
        CurWindow.prun_fac.setVisible(False)
        CurWindow.prun_acc.setVisible(False)

        CurWindow.pruning_dense.setVisible(False)
        CurWindow.pruning_conv.setVisible(False)
        CurWindow.pruning_conv_label.setVisible(False)
        CurWindow.pruning_dense_label.setVisible(False)

        CurWindow.min_acc.setVisible(False)
        CurWindow.acc_loss.setVisible(False)
        CurWindow.prun_acc_label.setVisible(False)
        CurWindow.prun_acc_edit.setVisible(False)


def set_quantization(self, CurWindow):
    """Adds or removes quantization from optimization.

    If "self.optimizations" doesn't contain quantization it gets added.
    Otherwise it gets removed. Furthermore the buttons for the
    quantization type appear or disappear.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    if CurWindow.quantization.isChecked():
        if "Quantization" not in self.optimizations:
            self.optimizations.append("Quantization")
        if self.quant_dtype is not None:
            if "int8 with float fallback" in self.quant_dtype:
                CurWindow.quant_int_only.setChecked(False)
                CurWindow.quant_int.setChecked(True)
            elif "int8 only" in self.quant_dtype:
                CurWindow.quant_int_only.setChecked(True)
                CurWindow.quant_int.setChecked(False)
        CurWindow.quant_int.setVisible(True)
        CurWindow.quant_int_only.setVisible(True)

    else:
        if "Quantization" in self.optimizations:
            self.optimizations.remove("Quantization")
        CurWindow.quant_int.setChecked(False)
        CurWindow.quant_int_only.setChecked(False)
        CurWindow.quant_int.setVisible(False)
        CurWindow.quant_int_only.setVisible(False)

    print("Optimizations:", self.optimizations)


def set_prun_type(self, prun_type, CurWindow, Pruning_button):
    """Sets the pruning type.

    Checks which button of the pruning type is pressed and
    sets it as pruning type.

    Args:
        prun_type:      Defines the pruning type.
        CurWindow:      GUI window from which the function is executed.
        Pruning_button: Was the Pruning button pressed or not
    """
    if "Factor" in prun_type:
        CurWindow.prun_acc.setChecked(False)
        CurWindow.min_acc.setChecked(False)
        CurWindow.acc_loss.setChecked(False)
        if (self.prun_type is None or "Factor" not in self.prun_type or
                Pruning_button):
            CurWindow.prun_fac.setChecked(True)
            self.prun_type = prun_type
            self.prun_acc_type = None
            if (self.prun_factor_dense is None and
                    self.prun_factor_conv is None):
                CurWindow.pruning_dense.setText("10")
                CurWindow.pruning_conv.setText("10")
            else:
                CurWindow.pruning_dense.setText(str(self.prun_factor_dense))
                CurWindow.pruning_conv.setText(str(self.prun_factor_conv))
            CurWindow.pruning_dense.setVisible(True)
            CurWindow.pruning_conv.setVisible(True)
            CurWindow.pruning_conv_label.setVisible(True)
            CurWindow.pruning_dense_label.setVisible(True)

            CurWindow.min_acc.setVisible(False)
            CurWindow.acc_loss.setVisible(False)
            CurWindow.prun_acc_label.setVisible(False)
            CurWindow.prun_acc_edit.setVisible(False)
        else:
            self.prun_type = None
            CurWindow.pruning_dense.setVisible(False)
            CurWindow.pruning_conv.setVisible(False)
            CurWindow.pruning_conv_label.setVisible(False)
            CurWindow.pruning_dense_label.setVisible(False)

    elif "Accuracy" in prun_type:
        CurWindow.prun_fac.setChecked(False)
        if (self.prun_type is None or "Accuracy" not in self.prun_type or
                Pruning_button):
            CurWindow.prun_acc.setChecked(True)
            self.prun_type = prun_type

            CurWindow.min_acc.setVisible(True)
            CurWindow.acc_loss.setVisible(True)

            print("Accuracy pruning type:", self.prun_acc_type)
            if (self.prun_acc_type is not None and
                    "Minimal accuracy" in self.prun_acc_type):
                CurWindow.min_acc.setChecked(True)
                CurWindow.acc_loss.setChecked(False)
                CurWindow.prun_acc_label.setText("Min accuracy\nto reach in %")
                CurWindow.prun_acc_label.setVisible(True)
                CurWindow.prun_acc_edit.setVisible(True)
                if self.prun_acc is None:
                    CurWindow.prun_acc_edit.setText("90")
                else:
                    CurWindow.prun_acc_edit.setText(str(self.prun_acc))

            elif (self.prun_acc_type is not None and
                    "Accuracy loss" in self.prun_acc_type):
                CurWindow.min_acc.setChecked(False)
                CurWindow.acc_loss.setChecked(True)
                CurWindow.prun_acc_label.setText("Max accuracy\nloss in %")
                CurWindow.prun_acc_label.setVisible(True)
                CurWindow.prun_acc_edit.setVisible(True)
                if self.prun_acc is None:
                    CurWindow.prun_acc_edit.setText("3")
                else:
                    CurWindow.prun_acc_edit.setText(str(self.prun_acc))

            try:
                self.prun_factor_dense = int(CurWindow.pruning_dense.text())
                self.prun_factor_conv = int(CurWindow.pruning_conv.text())
            except:
                self.prun_factor_dense = None
                self.prun_factor_conv = None
            CurWindow.pruning_dense.setVisible(False)
            CurWindow.pruning_conv.setVisible(False)
            CurWindow.pruning_conv_label.setVisible(False)
            CurWindow.pruning_dense_label.setVisible(False)
        else:
            self.prun_type = None
            self.prun_acc_type = None
            CurWindow.min_acc.setChecked(False)
            CurWindow.acc_loss.setChecked(False)

            CurWindow.min_acc.setVisible(False)
            CurWindow.acc_loss.setVisible(False)
            CurWindow.prun_acc_label.setVisible(False)
            CurWindow.prun_acc_edit.setVisible(False)
    print("Pruning type:", self.prun_type)


def set_prun_acc_type(self, prun_type, CurWindow):
    """Sets the pruning for accuracy type.

    Sets and unsets the checked pruning for accuracy type.

    Args:
        prun_acc_type: Defines the pruning for accuracy type.
        CurWindow:     GUI window from which the function is executed.
    """
    if "Minimal accuracy" in prun_type:
        CurWindow.acc_loss.setChecked(False)
        if (self.prun_acc_type is None or
                "Minimal accuracy" not in self.prun_acc_type):
            self.prun_acc_type = prun_type
            CurWindow.prun_acc_label.setVisible(True)
            CurWindow.prun_acc_label.setText("Min accuracy\nto reach in %")
            CurWindow.prun_acc_edit.setVisible(True)
            CurWindow.prun_acc_edit.setText("90")
            self.prun_acc = None
        else:
            self.prun_acc_type = None
            CurWindow.prun_acc_label.setVisible(False)
            CurWindow.prun_acc_edit.setVisible(False)
    elif "Accuracy loss" in prun_type:
        CurWindow.min_acc.setChecked(False)
        if (self.prun_acc_type is None or
                "Accuracy loss" not in self.prun_acc_type):
            self.prun_acc_type = prun_type
            CurWindow.prun_acc_label.setVisible(True)
            CurWindow.prun_acc_label.setText("Max accuracy\nloss in %")
            CurWindow.prun_acc_edit.setVisible(True)
            CurWindow.prun_acc_edit.setText("3")
            self.prun_acc = None
        else:
            self.prun_acc_type = None
            CurWindow.prun_acc_label.setVisible(False)
            CurWindow.prun_acc_edit.setVisible(False)
    print("Accuracy pruning type:", self.prun_acc_type)


def set_quant_dtype(self, dtype, CurWindow):
    """Sets the quantization type.

    Checks which button of the quantization type is pressed and
    sets it as quantization type.

    Args:
        dtype:     Defines the quantization type.
        CurWindow: GUI window from which the function is executed.
    """
    if "int8 with float fallback" in dtype:
        CurWindow.quant_int_only.setChecked(False)
        if not CurWindow.quant_int.isChecked():
            self.quant_dtype = None
        else:
            self.quant_dtype = dtype
    elif "int8 only" in dtype:
        CurWindow.quant_int.setChecked(False)
        if not CurWindow.quant_int_only.isChecked():
            self.quant_dtype = None
        else:
            self.quant_dtype = dtype
    print("Quantization type:", self.quant_dtype)


def model_pruning(self, CurWindow):
    """Starts the thread to prune the model.

    The thread for pruning the model is started. Also, the two
    buttons of the GUI window are hidden and the thread for the
    loading screen is started.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    CurWindow.summary.setVisible(False)
    CurWindow.project_name_label.setVisible(False)
    CurWindow.output_path_label.setVisible(False)
    CurWindow.model_path_label.setVisible(False)
    CurWindow.target_label.setVisible(False)
    CurWindow.optimizations_label.setVisible(False)
    CurWindow.pruning_label.setVisible(False)
    CurWindow.quantization_label.setVisible(False)
    CurWindow.data_loader_label.setVisible(False)
    CurWindow.model_memory_label.setVisible(False)
    CurWindow.model_memory.setVisible(False)
    CurWindow.model_memory_label_kb.setVisible(False)

    CurWindow.back.setVisible(False)
    CurWindow.load.setVisible(False)
    CurWindow.back_load_placeholder.setVisible(True)
    CurWindow.back_load_placeholder.setVisible(True)

    CurWindow.load_png.setVisible(True)

    CurWindow.loading_images.start()
    CurWindow.prune_model.start()


def convert_create(self, CurWindow):
    """Starts the thread to convert the model and create the project.

    The thread for pruning the model gets terminated and the thread
    to convert the model and create the project gets started.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    try:
        CurWindow.prune_model.stop_thread()
        if "MCU" in self.target:
            CurWindow.conv_build_load.set_model_memory(self.model_memory)
        CurWindow.conv_build_load.start()
    except:
        print("Error")


def terminate_thread(self, CurWindow):
    """End of converting the model and creating the project.

    Terminates the threads for pruning the model and converting the
    model and creating the project. Additionally, the "Finish" button
    becomes visible to close the GUI and the image of the loading
    screen signals the end of the process.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    try:
        print("Finish!")
        CurWindow.loading_images.stop_thread()
        CurWindow.conv_build_load.stop_thread()
        CurWindow.finish_placeholder.setVisible(False)
        CurWindow.finish.setVisible(True)
        CurWindow.load_png.setPixmap(QPixmap(os.path.join(
            "src", "GUILayout", "Images", "GUI_loading_images",
            "GUI_load_finish.png")))
        CurWindow.load_png.setScaledContents(True)
    except:
        print("Error")


def browse_csv_data(self, CurWindow):
    """Get the CSV file which contains your data.

    A Browse window opens and you can navigate to the CSV
    file which contains your data.
    """
    self.data_loader_path = QFileDialog.getOpenFileName(
        self, "Select your data loader script", os.path.expanduser('~'),
        'CSV(*.csv)')[0]
    print("CSV data path:", self.data_loader_path)

    CurWindow.table.setRowCount(0)
    CurWindow.table.setColumnCount(0)
    CurWindow.label_col.setVisible(False)
    CurWindow.cb_label_col.setVisible(False)
    CurWindow.tot_row.setVisible(False)
    CurWindow.num_row.setText("")
    CurWindow.tot_col.setVisible(False)
    CurWindow.num_col.setText("")


def preview_csv_data(self, CurWindow):
    """Gives a preview of the CSV data structure.

    Read the CSV file and separate the data according the selected
    separators. The data is represented by a table. Additionally, a
    drop-down list appears where the column of the data label can
    be selected. Also the number of rows and columns of the data get
    displayed.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    try:
        # Change shape of cursor to wait cursor
        QApplication.setOverrideCursor(Qt.WaitCursor)

        if (self.data_loader_path is not None and
                ".csv" in self.data_loader_path):
            self.get_separator(CurWindow)
            decimal = CurWindow.dec_label_col.currentText()
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
            CurWindow.table.setRowCount(df.shape[0])
            CurWindow.table.setColumnCount(df.shape[1])
            # returns pandas array object
            for row in df.iterrows():
                values = row[1]
                for col_index, value in enumerate(values):
                    tableItem = QTableWidgetItem(str(value))
                    CurWindow.table.setItem(row[0], col_index, tableItem)

            CurWindow.label_col.setVisible(True)
            CurWindow.cb_label_col.setVisible(True)

            CurWindow.tot_row.setVisible(True)
            CurWindow.num_row.setText(str(df.shape[0]))
            CurWindow.tot_col.setVisible(True)
            CurWindow.num_col.setText(str(df.shape[1]))

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


def load_csv_data(self, CurWindow, MainWindow):
    """Stores the target column of the CSV file and closes the window.
    """
    if CurWindow.cb_label_col.isVisible():
        self.csv_target_label = CurWindow.cb_label_col.currentText()
        self.decimal = CurWindow.dec_label_col.currentText()
        CurWindow.close()
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


def get_separator(self, CurWindow):
    """Read the selected separators.

    Checks if the different separator check boxes are checked or
    not. If a checkbox is selected, the corresponding separator is
    written to the variable "self.separator".

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    self.separator = None

    if CurWindow.cb_tab.isChecked():
        if self.separator is None:
            self.separator = r'\t'
        else:
            self.separator += r'|\t'
    if CurWindow.cb_semicolon.isChecked():
        if self.separator is None:
            self.separator = ';'
        else:
            self.separator += '|;'
    if CurWindow.cb_comma.isChecked():
        if self.separator is None:
            self.separator = ','
        else:
            self.separator += '|,'
    if CurWindow.cb_space.isChecked():
        if self.separator is None:
            self.separator = r'\s+'
        else:
            self.separator += r'|\s+'
    if CurWindow.cb_other.isChecked():
        if self.separator is None:
            self.separator = CurWindow.other_separator.text()
        else:
            self.separator += '|' + CurWindow.other_separator.text()

    print("CSV sperator:", self.separator)
