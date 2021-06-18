import os
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from src.Optimization.pruning import *
from src.GUIEvents._Helper import dataloader_pruning


class Prune_model(QThread):
    
    request_signal = pyqtSignal()
    
    def __init__(self, datascript_path, model_path, prun_factor_dense, prun_factor_conv, optimizations):
        QThread.__init__(self)
        self.datascript_path = datascript_path
        self.model_path = model_path
        self.prun_factor_dense = prun_factor_dense
        self.prun_factor_conv = prun_factor_conv
        self.optimizations = optimizations
        

    def run(self):
        if 'Pruning' in self.optimizations:
            model = tf.keras.models.load_model(self.model_path)
            num_classes = model.layers[-1].output_shape[1]

            x_train, x_val_y_train, label_one_hot = dataloader_pruning(self.datascript_path, model.input.shape[1], model.input.shape[2], model.input.shape[3], num_classes)

            pruned_model = prune_model(self.model_path, self.prun_factor_dense, self.prun_factor_conv, metric='L1',comp=None, num_classes=num_classes, label_one_hot=label_one_hot)
            
            train_epochs = 10
            callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)

            # fit model
            if os.path.isfile(self.datascript_path):
                print(x_train.shape)
                print(x_val_y_train.shape)
                pruned_model.fit(x=x_train, y=x_val_y_train, batch_size=64, validation_split=0.2,
                    epochs=train_epochs, callbacks=[callback])
            elif os.path.isdir(self.datascript_path):
                pruned_model.fit_generator(x_train, steps_per_epoch=len(x_train),
                    validation_data=x_val_y_train, validation_steps=len(x_val_y_train), epochs=train_epochs, callbacks=[callback])
                
            pruned_model.save(str(self.model_path[:-3]) + '_pruned.h5', include_optimizer=False)
        self.request_signal.emit()
        
    def stop_thread(self):
        self.terminate()