''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import sys
import os
import numpy as np
import random
from PIL import Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import tensorflow as tf

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def normalize_data(image,label):
    """Normalizes a given image to a range of 0 to 1.

    Args:
        image:  Image to normalize
        label:  Corresponding label to image

    Returns:
        Normalized images and corresponding labels
    """
    image = tf.cast(image/255. ,tf.float32)
    return image,label


def dataloader_quantization(data_loader_path, image_height, image_width, separator, csv_target_label):
    """Get Training data for quantization.

    Checks if your training data is inside a path or a file. Extracts
    the data from the directories or the file and returns it.

    Args:
        data_loader_path: Path or file of training data
        image_height:    Height of image
        image_width:     Width of image

    Returns:
        Training data which is needed for quantization.
    """
    train_images = []

    if os.path.isfile(data_loader_path):
        if ".csv" in data_loader_path:
            df = pd.read_csv(data_loader_path, sep=separator, index_col=False)

            if "First" in csv_target_label:
                X = np.array(df.iloc[:,1:].values)[..., np.newaxis]
            else:
                X = np.array(df.iloc[:,:-1].values)[..., np.newaxis]

            return X

        else:
            sys.path.append(os.path.dirname(data_loader_path))
            datascript = __import__(os.path.splitext(os.path.basename(data_loader_path))[0])
            x_train, _, _, _ = datascript.get_data()

        return x_train

    elif os.path.isdir(data_loader_path):

        classes = os.listdir(data_loader_path)
        print("Num classes: " + str(len(classes)))
        for folders in classes:
            if os.path.isdir(data_loader_path + "/" + folders):
                images = os.listdir(data_loader_path + "/" + folders)
            for i in range(0,int(500/len(classes))):
                rand_img = random.choice(images)
                img = Image.open(data_loader_path + "/" + folders + "/" + rand_img)
                resized_image = np.array(img.resize((image_height, image_width)))
                train_images.append(resized_image)
        
        train_images = np.asarray(train_images)
        if np.max(train_images) > 1:
            train_images = train_images/255.0
            
        if len(train_images.shape) == 3:
            train_images = np.expand_dims(train_images, axis=3) 

        return train_images


def dataloader_pruning(data_loader_path, separator, csv_target_label, image_height, image_width, num_channels, num_classes):
    """Get data for retraining the model after pruning.

    Checks if your data is inside a path or a file. Extracts the
    data from the directories or the file. If it is a file there
    is also a check if the label is one hot encoded or not. If it
    is a path data genarators are initialized.  

    Args:
        data_loader_path: Path or file of training data
        separator:       Delimiter to use
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
    if os.path.isfile(data_loader_path):
        if ".csv" in data_loader_path:
            df = pd.read_csv(data_loader_path, sep=separator, index_col=False)

            if "First" in csv_target_label:
                X = np.array(df.iloc[:,1:].values)[..., np.newaxis]
                Y = np.array(df.iloc[:,0].values).astype(np.int8)
            else:
                X = np.array(df.iloc[:,:-1].values)[..., np.newaxis]
                Y = np.array(df.iloc[:,-1].values).astype(np.int8)

            return X, Y, False

        else:
            sys.path.append(os.path.dirname(data_loader_path))
            datascript = __import__(os.path.splitext(os.path.basename(data_loader_path))[0])
            x_train, y_train, _, _ = datascript.get_data()
            if len(y_train.shape) > 1:
                label_one_hot = True
            else:
                label_one_hot = False
                
            return x_train, y_train, label_one_hot

    elif os.path.isdir(data_loader_path):
        # create data generator
        train_datagen = ImageDataGenerator(validation_split=0.2)
        # prepare iterators
        if num_channels == 1:
            color_mode = 'grayscale'
        elif num_channels == 3:
            color_mode = 'rgb'
            
        if num_classes > 2:
            class_mode = 'sparse'
        else:
            class_mode = 'binary'

        train_it = train_datagen.flow_from_directory(data_loader_path, target_size=(image_height, image_width), color_mode=color_mode, class_mode=class_mode, batch_size=128, subset='training')
        val_it = train_datagen.flow_from_directory(data_loader_path, target_size=(image_height, image_width), color_mode=color_mode, class_mode=class_mode, batch_size=128, subset='validation')

        if next(iter(val_it))[0].numpy().max() > 1.0:
            train_it = val_it.map(normalize_data)
            val_it = val_it.map(normalize_data)

        return train_it, val_it, False