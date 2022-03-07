'''Copyright [2020] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
   Copyright [2022] Hahn-Schickard-Gesellschaft fuer angewandte Forschung e.V.,
                    Daniel Konegen + Marcus Rueb
   SPDX-License-Identifier: Apache-2.0
============================================================================'''

import sys
import os
import numpy as np
import random
from PIL import Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import tensorflow as tf
import autokeras as ak
from sklearn.model_selection import train_test_split

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def normalize_data(image, label):
    """Normalizes a given image to a range of 0 to 1.

    Args:
        image:  Image to normalize
        label:  Corresponding label to image

    Returns:
        Normalized images and corresponding labels
    """
    image = tf.cast(image / 255., tf.float32)
    return image, label


def modify_labels(image, label):
    """Turn labels from string values to integer values.

    Args:
        image:  Image of dataloader
        label:  label to convert

    Returns:
        Converted label and corresponding image
    """
    for item in label_list:
        label = tf.strings.regex_replace(label, item, str(label_dict[item]))
    label = tf.strings.to_number(label)
    label = tf.cast(label, tf.int8)

    return image, label


def dataloader_quantization(data_loader_path, img_height, img_width, separator,
                            decimal, csv_target_label):
    """Get Training data for quantization.

    Checks if your training data is inside a path or a file. Extracts
    the data from the directories or the file and returns it.

    Args:
        data_loader_path:   Path or file of training data
        img_height:         Height of image
        img_width:          Width of image
        separator:          Separator for reading a CSV file
        decimal:            Decimal for reading a CSV file
        csv_target_label:   Target label from the CSV file

    Returns:
        Training data which is needed for quantization.
    """
    train_images = []

    if os.path.isfile(data_loader_path):
        if ".csv" in data_loader_path:
            df = pd.read_csv(data_loader_path, sep=separator, decimal=decimal,
                             index_col=False, dtype=np.float32)

            if "First" in csv_target_label:
                X = np.array(df.iloc[:, 1:].values)[..., np.newaxis]
            else:
                X = np.array(df.iloc[:, :-1].values)[..., np.newaxis]

            return X

        else:
            sys.path.append(os.path.dirname(data_loader_path))
            datascript = __import__(os.path.splitext(
                os.path.basename(data_loader_path))[0])
            x_train, _, _, _ = datascript.get_data()

        return x_train

    elif os.path.isdir(data_loader_path):

        classes = os.listdir(data_loader_path)
        print("Num classes: " + str(len(classes)))
        for folders in classes:
            if os.path.isdir(data_loader_path + "/" + folders):
                images = os.listdir(data_loader_path + "/" + folders)
            for i in range(0, int(500 / len(classes))):
                rand_img = random.choice(images)
                img = Image.open(data_loader_path + "/" + folders + "/" +
                                 rand_img)
                resized_image = np.array(img.resize((img_height, img_width)))
                train_images.append(resized_image)

        train_images = np.asarray(train_images)
        if np.max(train_images) > 1:
            train_images = train_images / 255.0

        if len(train_images.shape) == 3:
            train_images = np.expand_dims(train_images, axis=3)

        return train_images


def dataloader_pruning(data_loader_path, separator, decimal, csv_target_label,
                       img_height, img_width, num_channels, num_classes):
    """Get data for retraining the model after pruning.

    Checks if your data is inside a path or a file. Extracts the
    data from the directories or the file. If it is a file there
    is also a check if the label is one hot encoded or not. If it
    is a path data genarators are initialized.

    Args:
        data_loader_path:   Path or file of training data
        separator:          Delimiter to use
        decimal:            Decimal for reading a CSV file
        csv_target_label:   Target label from the CSV file
        img_height:         Height of image
        img_width:          Width of image
        num_channels:       Number of channels of the image
        num_classes:        Number of different classes of the model

    Returns:
        If the dataloader is a file training data, the labels and
        whether the label is one hot encoded or not is returned.
        If the dataloader is a path the datagenerators for training
        and validation data is returned. Furthermore "False" is
        returned, because it is not one hot encoded.
    """
    if os.path.isfile(data_loader_path):
        if ".csv" in data_loader_path:
            df = pd.read_csv(data_loader_path, sep=separator, decimal=decimal,
                             index_col=False, dtype=np.float32)

            if "First" in csv_target_label:
                X = np.array(df.iloc[:, 1:].values)[..., np.newaxis]
                Y = np.array(df.iloc[:, 0].values).astype(np.int8)
            else:
                X = np.array(df.iloc[:, :-1].values)[..., np.newaxis]
                Y = np.array(df.iloc[:, -1].values).astype(np.int8)

            return X, Y, False

        else:
            sys.path.append(os.path.dirname(data_loader_path))
            datascript = __import__(os.path.splitext(os.path.basename(
                data_loader_path))[0])
            x_train, y_train, _, _ = datascript.get_data()
            if len(y_train.shape) > 1:
                label_one_hot = True
            else:
                label_one_hot = False

            return x_train, y_train, label_one_hot

    elif os.path.isdir(data_loader_path):
        # Check if image values are normalized or not
        rand_class = random.choice(os.listdir(data_loader_path))
        images = os.listdir(data_loader_path + "/" + rand_class)
        rand_img = random.choice(images)
        img = Image.open(data_loader_path + "/" + rand_class + "/" + rand_img)
        # create data generator
        if np.asarray(img).max() > 1.0:
            train_datagen = ImageDataGenerator(rescale=1.0 / 255.0,
                                               validation_split=0.2)
        else:
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

        train_it = train_datagen.flow_from_directory(
            data_loader_path, target_size=(img_height, img_width),
            color_mode=color_mode, class_mode=class_mode, batch_size=128,
            subset='training')
        val_it = train_datagen.flow_from_directory(
            data_loader_path, target_size=(img_height, img_width),
            color_mode=color_mode, class_mode=class_mode, batch_size=128,
            subset='validation')

        return train_it, val_it, False


def dataloader_autokeras(data_loader_path, separator, decimal,
                         csv_target_label, img_height, img_width,
                         num_channels):
    """Get data for of model using AutoKeras.

    Checks if your data is inside a path or a file. Extracts the
    data from the directories or the file. If it is a file there
    is also a check if the label is one hot encoded or not. If it
    is a path data genarators are initialized.

    Args:
        data_loader_path:   Path or file of training data
        separator:          Delimiter to use
        decimal:            Decimal for reading a CSV file
        csv_target_label:   Target label from the CSV file
        img_height:         Height of image
        img_width:          Width of image
        num_channels:       Number of channels of the image

    Returns:
        Returns the data for training models as datagenerators
        or as numpy arrays depending on if the data loader
        path is a file or directory.
    """
    if os.path.isfile(data_loader_path):
        if ".csv" in data_loader_path:
            df = pd.read_csv(data_loader_path, sep=separator, decimal=decimal,
                             index_col=False, dtype=np.float32)

            if "First" in csv_target_label:
                X = np.array(df.iloc[:, 1:].values)[..., np.newaxis]
                Y = np.array(df.iloc[:, 0].values).astype(np.int8)
            else:
                X = np.array(df.iloc[:, :-1].values)[..., np.newaxis]
                Y = np.array(df.iloc[:, -1].values).astype(np.int8)

            x_train, x_test, y_train, y_test = train_test_split(
                X, Y, test_size=0.2, shuffle=True,)
            print("Type data:", x_train.dtype)

        else:
            sys.path.append(os.path.dirname(data_loader_path))
            datascript = __import__(os.path.splitext(
                os.path.basename(data_loader_path))[0])
            x_train, y_train, x_test, y_test = datascript.get_data()

        return x_train, y_train, x_test, y_test

    elif os.path.isdir(data_loader_path):
        if num_channels == 1:
            color_mode = 'grayscale'
        elif num_channels == 3:
            color_mode = 'rgb'
        else:
            print("Choose a valid number of channels")
            return

        train_data = ak.image_dataset_from_directory(
            data_loader_path,
            # Use 20% data as testing data.
            validation_split=0.2,
            subset="training",
            # Set seed to ensure the same split when loading testing data.
            seed=123,
            image_size=(img_height, img_width),
            color_mode=color_mode,
            batch_size=128,
            shuffle=True,
        )

        test_data = ak.image_dataset_from_directory(
            data_loader_path,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=(img_height, img_width),
            color_mode=color_mode,
            batch_size=128,
            shuffle=True,
        )

        if next(iter(train_data))[0].numpy().max() > 1.0:
            train_data = train_data.map(normalize_data)
            test_data = test_data.map(normalize_data)

        # Turn string labels to int values
        classes = os.listdir(data_loader_path)
        global label_dict
        label_dict = dict([(y, x) for x, y in enumerate(sorted(set(classes)))])
        global label_list
        label_list = list(label_dict.keys())

        train_data = train_data.map(modify_labels)
        test_data = test_data.map(modify_labels)

        return train_data, None, test_data, None
