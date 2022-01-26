"""This is a splittet method from the Mainwindow class which contain the logic for the AutoMLData window

The programmed logic in this method defines the workflow and path for the GUI. Especially

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""

import sys
import os
import matplotlib.image as mpimg
import numpy as np
import random
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import csv
import pandas as pd
import math
import tensorflow as tf

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def get_output_path(self, CurWindow):
    """Get the path where the genareted Project should be stored

    A Browse window opens and you can navigate to the directory
    you wanna store the project.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    self.output_path = QFileDialog.getExistingDirectory(
        self, "Select the output path", "./"
    )
    CurWindow.Output_Pfad.setText(self.output_path)
    print(CurWindow.Output_Pfad.text())

def get_model_path(self, CurWindow):
    """Get the keras model which should be converted

    A Browse window opens and you can navigate to the keras
    model file you wanna convert to TensorFlow lite for
    microcontrollers.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    self.model_path = QFileDialog.getOpenFileName(self, "Select your model", "./")[0]
    CurWindow.Model_Pfad.setText(self.model_path)
    print(CurWindow.Model_Pfad.text())

def get_data_loader(self, CurWindow):
    """Get the file or path to load your training data.

    A Browse window opens and you can navigate to the directory
    containing your training data. Otherwise you can select a file
    which loads your training. If the file is a CSV the 
    CSVDataloaderWindow() function is executed. 

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    if "Select PATH with data" in CurWindow.dataloader_list.currentText():
        self.data_loader_path = QFileDialog.getExistingDirectory(
            self, "Select your trainingdata path", "./"
        )
    elif "Select SCRIPT with data" in CurWindow.dataloader_list.currentText():
        self.data_loader_path = QFileDialog.getOpenFileName(
            self, "Select your data loader script", "./"
        )[0]
    CurWindow.Daten_Pfad.setText(self.data_loader_path)
    print(CurWindow.Daten_Pfad.text())

    if ".csv" in self.data_loader_path:
        print("SIE HABEN EINE CSV-DATEI AUSGEWÄHLT")
    else:
        print("KEINE CSV-DATEI")

def set_pruning(self, CurWindow):
    """Adds or removes pruning from optimization.

    If "self.optimizations" doesn't contain pruning it gets added.
    Otherwise it gets removed. Furthermore the input fields for the
    pruning factors appear or disappear.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    if CurWindow.Pruning.isChecked() == True:
        if not "Pruning" in self.optimizations:
            self.optimizations.append("Pruning")
            print(self.optimizations)
        if self.prun_factor_dense == None and self.prun_factor_conv == None:
            CurWindow.Pruning_Dense.setText("10")
            CurWindow.Pruning_Conv.setText("10")
        else:
            CurWindow.Pruning_Dense.setText(str(self.prun_factor_dense))
            CurWindow.Pruning_Conv.setText(str(self.prun_factor_conv))
        CurWindow.Pruning_Dense.setVisible(True)
        CurWindow.Pruning_Conv.setVisible(True)
        CurWindow.Pruning_Conv_label.setVisible(True)
        CurWindow.Pruning_Dense_label.setVisible(True)

        CurWindow.Pruning.setIconSize(QSize(100, 100))
        CurWindow.Pruning.setGeometry(145, 85, 120, 120)

    else:
        if "Pruning" in self.optimizations:
            self.optimizations.remove("Pruning")
            print(self.optimizations)
        try:
            self.prun_factor_dense = int(CurWindow.Pruning_Dense.text())
            self.prun_factor_conv = int(CurWindow.Pruning_Conv.text())
        except:
            self.prun_factor_dense = None
            self.prun_factor_conv = None
        CurWindow.Pruning_Dense.setVisible(False)
        CurWindow.Pruning_Conv.setVisible(False)
        CurWindow.Pruning_Conv_label.setVisible(False)
        CurWindow.Pruning_Dense_label.setVisible(False)

        CurWindow.Pruning.setIconSize(QSize(150, 150))
        CurWindow.Pruning.setGeometry(120, 85, 170, 170)

def set_quantization(self, CurWindow):
    """Adds or removes quantization from optimization.

    If "self.optimizations" doesn't contain quantization it gets added.
    Otherwise it gets removed. Furthermore the buttons for the
    quantization type appear or disappear.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    if CurWindow.Quantization.isChecked() == True:
        if not "Quantization" in self.optimizations:
            self.optimizations.append("Quantization")
            print(self.optimizations)
        if self.quant_dtype != None:
            if "int8 with float fallback" in self.quant_dtype:
                CurWindow.quant_int_only.setChecked(False)
                CurWindow.quant_int.setChecked(True)
            elif "int8 only" in self.quant_dtype:
                CurWindow.quant_int_only.setChecked(True)
                CurWindow.quant_int.setChecked(False)
        CurWindow.quant_int.setVisible(True)
        CurWindow.quant_int_only.setVisible(True)

        CurWindow.Quantization.setIconSize(QSize(100, 100))
        CurWindow.Quantization.setGeometry(540, 85, 120, 120)

    else:
        if "Quantization" in self.optimizations:
            self.optimizations.remove("Quantization")
            print(self.optimizations)
        CurWindow.quant_int.setChecked(False)
        CurWindow.quant_int_only.setChecked(False)
        CurWindow.quant_int.setVisible(False)
        CurWindow.quant_int_only.setVisible(False)

        CurWindow.Quantization.setIconSize(QSize(150, 150))
        CurWindow.Quantization.setGeometry(515, 85, 170, 170)

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
        if CurWindow.quant_int.isChecked() == False:
            self.quant_dtype = None
        else:
            self.quant_dtype = dtype
    elif "int8 only" in dtype:
        CurWindow.quant_int.setChecked(False)
        if CurWindow.quant_int_only.isChecked() == False:
            self.quant_dtype = None
        else:
            self.quant_dtype = dtype
    print(self.quant_dtype)

def set_knowledge_distillation(self, CurWindow):
    """Adds or removes knonwledge distillation from optimization.

    If "self.optimizations" doesn't contain konwledge distillation
    it gets added. Otherwise it gets removed.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    if CurWindow.Dis.isChecked() == True:
        if not "Knowledge_Distillation" in self.optimizations:
            self.optimizations.append("Knowledge_Distillation")
            print(self.optimizations)
        CurWindow.Dis_1.setText("10")
        CurWindow.Dis_2.setText("10")
        CurWindow.Dis_1.setVisible(True)
        CurWindow.Dis_2.setVisible(True)
        CurWindow.Dis_1_label.setVisible(True)
        CurWindow.Dis_2_label.setVisible(True)

        CurWindow.Dis.setIconSize(QSize(100, 100))
        CurWindow.Dis.setGeometry(145, 320, 120, 120)

    else:
        if "Knowledge_Distillation" in self.optimizations:
            self.optimizations.remove("Knowledge_Distillation")
            print(self.optimizations)
        CurWindow.Dis_1.setVisible(False)
        CurWindow.Dis_2.setVisible(False)
        CurWindow.Dis_1_label.setVisible(False)
        CurWindow.Dis_2_label.setVisible(False)

        CurWindow.Dis.setIconSize(QSize(150, 150))
        CurWindow.Dis.setGeometry(120, 320, 170, 170)

def set_huffman_coding(self, CurWindow):
    """Adds or removes huffman coding from optimization.

    If "self.optimizations" doesn't contain huffman coding it 
    gets added. Otherwise it gets removed.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    if CurWindow.Huf.isChecked() == True:
        if not "Huffman_Coding" in self.optimizations:
            self.optimizations.append("Huffman_Coding")
            print(self.optimizations)
        CurWindow.Huf_1.setText("10")
        CurWindow.Huf_2.setText("10")
        CurWindow.Huf_1.setVisible(True)
        CurWindow.Huf_2.setVisible(True)
        CurWindow.Huf_1_label.setVisible(True)
        CurWindow.Huf_2_label.setVisible(True)

        CurWindow.Huf.setIconSize(QSize(100, 100))
        CurWindow.Huf.setGeometry(540, 320, 120, 120)

    else:
        if "Huffman_Coding" in self.optimizations:
            self.optimizations.remove("Huffman_Coding")
            print(self.optimizations)
        CurWindow.Huf_1.setVisible(False)
        CurWindow.Huf_2.setVisible(False)
        CurWindow.Huf_1_label.setVisible(False)
        CurWindow.Huf_2_label.setVisible(False)

        CurWindow.Huf.setIconSize(QSize(150, 150))
        CurWindow.Huf.setGeometry(515, 320, 170, 170)

def get_optimization(self, button):
    """Returns the selected optimizations.

    Returns the selected optimizations according to the
    button of the optimizaiton type is pressed or not.

    Args:
        button: Pruning or quantization button.
    """
    if button.text() == "Pruning":
        if button.isChecked() == True:
            if not "Pruning" in self.optimizations:
                self.optimizations.append(button.text())
            # print(button.text() " is selected")
        else:
            if "Pruning" in self.optimizations:
                self.optimizations.remove(button.text())
            # print(button.text() " is deselected")

    if button.text() == "Quantization":
        if button.isChecked() == True:
            if not "Quantization" in self.optimizations:
                self.optimizations.append(button.text())
            # print(button.text() " is selected")
        else:
            if "Quantization" in self.optimizations:
                self.optimizations.remove(button.text())
            # print(button.text() " is deselected")

    print(self.optimizations)

# def set_optimizations(self, optimizations, CurWindow):
#     if "Pruning" in optimizations:
#         CurWindow.b[0].setChecked(True)

#     if "Quantization" in optimizations:
#         CurWindow.b[1].setChecked(True)

def model_pruning(self, CurWindow):
    """Starts the thread to prune the model.

    The thread for pruning the model is started. Also, the two 
    buttons of the GUI window are hidden and the thread for the 
    loading screen is started.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    CurWindow.Back.setVisible(False)
    CurWindow.Load.setVisible(False)

    CurWindow.loading_images.start()
    CurWindow.prune_model.start()

def download(self, CurWindow):
    """Starts the thread to convert the model and create the project.

    The thread for pruning the model gets terminated and the thread
    to convert the model and create the project gets started.

    Args:
        CurWindow: GUI window from which the function is executed.
    """
    try:
        if "uC" in self.target:
            CurWindow.prune_model.stop_thread()
            print("To uC start")
            CurWindow.conv_build_load.start()

        if "FPGA" in self.target:
            CurWindow.prune_model.stop_thread()
            print("To FPGA start")
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
        CurWindow.Finish.setVisible(True)
        CurWindow.Loadpng.setPixmap(
            QPixmap(
                os.path.join(
                    "Images", "GUI_loading_images", "GUI_load_finish.png"
                )
            )
        )
    except:
        print("Error")


def dataloader_quantization(datascript_path, image_height, image_width):
    """Get Training data for quantization.

    Checks if your training data is inside a path or a file. Extracts
    the data from the directories or the file and returns it.

    Args:
        datascript_path: Path or file of training data
        image_height:    Height of image
        image_width:     Width of image

    Returns:
        Training data which is needed for quantization.
    """
    train_images = []

    if os.path.isfile(datascript_path):
        sys.path.append(os.path.dirname(datascript_path))
        datascript = __import__(os.path.splitext(os.path.basename(datascript_path))[0])
        x_train, _, _, _ = datascript.get_data()

        return x_train

    elif os.path.isdir(datascript_path):

        classes = os.listdir(datascript_path)
        print("Num classes: " + str(len(classes)))
        for folders in classes:
            if os.path.isdir(datascript_path + "/" + folders):
                images = os.listdir(datascript_path + "/" + folders)
            for i in range(0,int(500/len(classes))):
                rand_img = random.choice(images)
                img = mpimg.imread(datascript_path + "/" + folders + "/" + rand_img)
                resized_image = cv2.resize(img, (image_height, image_width))
                train_images.append(resized_image)
        
        train_images = np.asarray(train_images)
        if len(train_images.shape) == 3:
            train_images = np.expand_dims(train_images, axis=3) 

        return train_images



def dataloader_pruning(datascript_path, image_height, image_width, num_channels, num_classes):
    """Get data for retraining the model after pruning.

    Checks if your data is inside a path or a file. Extracts the
    data from the directories or the file. If it is a file there
    is also a check if the label is one hot encoded or not. If it
    is a path data genarators are initialized.  

    Args:
        datascript_path: Path or file of training data
        image_height:    Height of image
        image_width:     Width of image
        num_channels:    Number of channels of the image
        num_classes:     Number of different classes of the model

    Returns:
        If the dataloader is a file training data, the labels and
        whether the label is one hot encoded or not is returned.
        If the dataloader is a path the datagenerators for training
        and validation data is returned. Furthermore "False" is
        returned, because it is not one hot encoded. 
    """
    if os.path.isfile(datascript_path):
        print("IST EINE DATEI")
        sys.path.append(os.path.dirname(datascript_path))
        datascript = __import__(os.path.splitext(os.path.basename(datascript_path))[0])
        x_train, y_train, _, _ = datascript.get_data()
        print("SHAPE!!")
        print(len(y_train.shape))
        if len(y_train.shape) > 1:
            label_one_hot = True
        else:
            label_one_hot = False
            
        return x_train, y_train, label_one_hot

    elif os.path.isdir(datascript_path):

        print(num_channels)

        # create data generator
        train_datagen = ImageDataGenerator(rescale=1.0/255.0, validation_split=0.2)
        # prepare iterators
        if num_channels == 1:
            if num_classes > 2:
                train_it = train_datagen.flow_from_directory(datascript_path, target_size=(image_height, image_width), color_mode='grayscale', class_mode='sparse', batch_size=64, subset='training')
                val_it = train_datagen.flow_from_directory(datascript_path, target_size=(image_height, image_width), color_mode='grayscale', class_mode='sparse', batch_size=64, subset='validation')
            else:
                train_it = train_datagen.flow_from_directory(datascript_path, target_size=(image_height, image_width), color_mode='grayscale', class_mode='binary', batch_size=64, subset='training')
                val_it = train_datagen.flow_from_directory(datascript_path, target_size=(image_height, image_width), color_mode='grayscale', class_mode='binary', batch_size=64, subset='validation')
        
        elif num_channels == 3:
            if num_classes > 2:
                train_it = train_datagen.flow_from_directory(datascript_path, target_size=(image_height, image_width), color_mode='rgb', class_mode='sparse', batch_size=64, subset='training')
                val_it = train_datagen.flow_from_directory(datascript_path, target_size=(image_height, image_width), color_mode='rgb', class_mode='sparse', batch_size=64, subset='validation')
            else:
                train_it = train_datagen.flow_from_directory(datascript_path, target_size=(image_height, image_width), color_mode='rgb', class_mode='binary', batch_size=64, subset='training')
                val_it = train_datagen.flow_from_directory(datascript_path, target_size=(image_height, image_width), color_mode='rgb', class_mode='binary', batch_size=64, subset='validation')

        return train_it, val_it, False



class ThresholdCallback(tf.keras.callbacks.Callback):
    """Custom callback for model training.

    This is a custom callback function. You can define an accuracy threshold
    value when the model training should be stopped.

    Attributes:
        threshold: Accuracy value to stop training.
    """

    def __init__(self, threshold):
        super(ThresholdCallback, self).__init__()
        self.threshold = threshold

    def on_epoch_end(self, epoch, logs=None): 
        val_acc = logs["val_accuracy"]        
        if val_acc >= self.threshold:
            self.model.stop_training = True