''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import autokeras as ak
import os
import tensorflow as tf

from src.GUIEvents._DataloaderHelper import dataloader_autokeras


def data_regressor(project_name, output_path, data_path, max_trials=10, max_epochs=20, max_size=0, overwrite=True,
            separator=None, decimal=None, csv_target_label=None):

    input_node = ak.Input()
    output_node = ak.DenseBlock()(input_node)
    output_node = ak.RegressionHead()(output_node)
    clf = ak.AutoModel(
        inputs=input_node, outputs=output_node, overwrite=overwrite, max_trials=max_trials, max_model_size=max_size
    )
    
    if os.path.isfile(data_path):
        x_train, y_train, x_test, y_test = dataloader_autokeras(data_path, separator, decimal, csv_target_label,
                                                    None, None, None)
        clf.fit(x_train, y_train, epochs=max_epochs, validation_split=0.2,
                callbacks=[tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)])
        # Evaluate the best model with testing data.
        print("Best model evaluation:",clf.evaluate(x_test, y_test))
    elif os.path.isdir(data_path):
        print("For data regression select a file as data loader.")
        return

    best = clf.export_model()
    best.summary()
    
    best.save(output_path + "/" +  project_name + '.h5')