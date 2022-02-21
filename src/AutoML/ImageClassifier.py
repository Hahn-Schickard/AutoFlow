''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

from random import shuffle
import autokeras as ak
import os
import tensorflow as tf

from src.GUIEvents._DataloaderHelper import dataloader_autokeras


def image_classifier(project_name, output_path, data_path, max_trials=10, max_epochs=20, max_size=0, overwrite=True, 
            num_channels=3, img_height=128, img_width=128, separator=None, decimal=None, csv_target_label=None):

    input_node = ak.ImageInput()
    output_node = ak.ConvBlock()(input_node)
    output_node = ak.DenseBlock()(output_node)
    output_node = ak.ClassificationHead()(output_node)
    clf = ak.AutoModel(
        inputs=input_node, outputs=output_node, overwrite=overwrite, max_trials=max_trials, max_model_size=max_size
    )
    
    if os.path.isfile(data_path):
        x_train, y_train, x_test, y_test = dataloader_autokeras(data_path, separator, decimal, csv_target_label,
                                                    img_height, img_width, num_channels)
        clf.fit(x_train, y_train, epochs=max_epochs, validation_split=0.2, shuffle=True,
                callbacks=[tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)])
        # Evaluate the best model with testing data.
        print(clf.evaluate(x_test, y_test))
    elif os.path.isdir(data_path):
        train_data, _, test_data, _ = dataloader_autokeras(data_path, separator, decimal, csv_target_label,
                                                img_height, img_width, num_channels)
        clf.fit(train_data, epochs=max_epochs, validation_split=0.2, shuffle=True,
                callbacks=[tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)])
        # Evaluate the best model with testing data.
        print(clf.evaluate(test_data))

    best = clf.export_model()
    best.summary()
    
    best.save(output_path + "/" +  project_name + '.h5')