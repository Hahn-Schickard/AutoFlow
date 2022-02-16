''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    Copyright [2021] Karlsruhe Institute of Technology, Daniel Konegen
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import os
import sys
import tensorflow as tf
sys.path.append("..") # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.Optimization.pruning import prune_model, pruning_for_acc
from src.GUIEvents._DataloaderHelper import dataloader_pruning


class Prune_model(QThread):
    """Thread to prune and retrain the model.

    Attributes:
        model_path:        Path of the model to convert
        data_loader_path:  Path of the folder or file with the training data
        optimizations:     Selected optimization algorithms
        prun_type:         Type of pruning
        prun_factor_dense: Pruning factor for fully connected layers
        prun_factor_conv:  Pruning factor for convolution layers
        prun_acc_type:     Type of pruning to accuracy
        prun_acc:          Accuracy to prune to
        separator:         Separator for reading a CSV file
        csv_target_label:  Target label from the CSV file
    """
    
    request_signal = pyqtSignal()
    
    def __init__(self, model_path, data_loader_path, optimizations, prun_type, prun_factor_dense, prun_factor_conv, prun_acc_type, prun_acc, separator, csv_target_label):
        QThread.__init__(self)
        self.model_path = model_path
        self.data_loader_path = data_loader_path
        self.optimizations = optimizations
        self.prun_type = prun_type
        self.prun_factor_dense = prun_factor_dense
        self.prun_factor_conv = prun_factor_conv
        self.prun_acc_type = prun_acc_type
        self.prun_acc = prun_acc
        self.separator = separator
        self.csv_target_label = csv_target_label
        

    def run(self):
        """Activates the thread

        If pruning was defined as an optimization algorithm, pruning will
        be performed. The model is loaded, pruned and then re-trained.
        When the function is finished, a signal is emitted.
        """          
        if 'Pruning' in self.optimizations:
            model = tf.keras.models.load_model(self.model_path)
            num_classes = model.layers[-1].output_shape[1]

            if len(model.input.shape) <= 3:
                x_train, x_val_y_train, label_one_hot = dataloader_pruning(self.data_loader_path, self.separator, self.csv_target_label, model.input.shape[1], model.input.shape[2], None, num_classes)
            else:
                x_train, x_val_y_train, label_one_hot = dataloader_pruning(self.data_loader_path, self.separator, self.csv_target_label, model.input.shape[1], model.input.shape[2], model.input.shape[3], num_classes)

            #The compiler could also get included to the GUI
            if num_classes <= 2:
                comp = {
                "optimizer": 'adam',
                "loss": tf.keras.losses.BinaryCrossentropy(),
                "metrics": 'accuracy'}    
            else:
                if label_one_hot == True:
                    comp = {
                    "optimizer": 'adam',
                    "loss": tf.keras.losses.CategoricalCrossentropy(),
                    "metrics": 'accuracy'}  
                else:
                    comp = {
                    "optimizer": 'adam',
                    "loss": tf.keras.losses.SparseCategoricalCrossentropy(),
                    "metrics": 'accuracy'}

            if "Factor" in self.prun_type:
                pruned_model = prune_model(model, self.prun_factor_dense, self.prun_factor_conv, metric='L1',comp=comp, num_classes=num_classes, label_one_hot=label_one_hot)
            else:
                if "Minimal accuracy" in self.prun_acc_type:
                    pruned_model = pruning_for_acc(model, x_train, x_val_y_train, comp=comp, pruning_acc=self.prun_acc, max_acc_loss=None, num_classes=num_classes, label_one_hot=label_one_hot, data_loader_path=self.data_loader_path)
                else:
                    pruned_model = pruning_for_acc(model, x_train, x_val_y_train, comp=comp, pruning_acc=None, max_acc_loss=self.prun_acc, num_classes=num_classes, label_one_hot=label_one_hot, data_loader_path=self.data_loader_path)


            train_epochs = 20
            callback = tf.keras.callbacks.EarlyStopping(monitor='val_accuracy', patience=5, restore_best_weights=True)

            pruned_model.summary()

            # fit model
            if os.path.isfile(self.data_loader_path):
                pruned_model.fit(x=x_train, y=x_val_y_train, batch_size=64, validation_split=0.2,
                    epochs=train_epochs, callbacks=[callback])
            elif os.path.isdir(self.data_loader_path):
                pruned_model.fit_generator(x_train, steps_per_epoch=len(x_train),
                    validation_data=x_val_y_train, validation_steps=len(x_val_y_train), epochs=train_epochs, callbacks=[callback])
                
            pruned_model.save(str(self.model_path[:-3]) + '_pruned.h5', include_optimizer=False)
        self.request_signal.emit()
        
    def stop_thread(self):
        """Ends the thread
        """
        self.terminate()