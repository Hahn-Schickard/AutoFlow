''' Copyright [2020] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Marcel Sawrin + Marcus Rueb
    Copyright [2022] Hahn-Schickard-Gesellschaft für angewandte Forschung e.V., Daniel Konegen + Marcus Rueb
    SPDX-License-Identifier: Apache-2.0
============================================================================================================'''

import autokeras as ak
from tensorflow.keras.datasets import cifar10
import argparse
import importlib.util
import shutil
import os
import sys
import tensorflow as tf

from src.GUIEvents._DataloaderHelper import normalize_data


def ImageClassifier(ProjectName, OutputPath, DataPath, MaxTrials=10, MaxEpochs=20, MaxSize=0, Overwrite=True, NumChannels=3, ImgHeight=128, ImgWidth=128):

    if os.path.isfile(DataPath):
        if ".csv" in DataPath:
            pass
            # df = pd.read_csv(data_loader_path, sep=separator, index_col=False)

            # if "First" in csv_target_label:
            #     X = np.array(df.iloc[:,1:].values)[..., np.newaxis]
            #     Y = np.array(df.iloc[:,0].values).astype(np.int8)
            # else:
            #     X = np.array(df.iloc[:,:-1].values)[..., np.newaxis]
            #     Y = np.array(df.iloc[:,-1].values).astype(np.int8)

            # return X, Y, False

        else:
            spec = importlib.util.spec_from_file_location("module.name", DataPath)
            datascript = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(datascript)
            x_train, y_train, x_test, y_test = datascript.get_data()

    elif os.path.isdir(DataPath):
        if NumChannels == 1:
            color_mode = 'grayscale'
        elif NumChannels == 3:
            color_mode = 'rgb'
        else:
            print("Choose a valid number of channels")
            return

        train_data = ak.image_dataset_from_directory(
            DataPath,
            # Use 20% data as testing data.
            validation_split=0.2,
            subset="training",
            # Set seed to ensure the same split when loading testing data.
            seed=123,
            image_size=(ImgHeight, ImgWidth),
            color_mode=color_mode,
            batch_size=128,
        )

        test_data = ak.image_dataset_from_directory(
            DataPath,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=(ImgHeight, ImgWidth),
            color_mode=color_mode,
            batch_size=128,
        )

    if next(iter(train_data))[0].numpy().max() > 1.0:
        train_data = train_data.map(normalize_data)
        test_data = test_data.map(normalize_data)


    input_node = ak.ImageInput()
    output_node = ak.ConvBlock()(input_node)
    output_node = ak.DenseBlock()(output_node)
    output_node = ak.ClassificationHead()(output_node)
    clf = ak.AutoModel(
        inputs=input_node, outputs=output_node, overwrite=Overwrite, max_trials=MaxTrials, max_model_size=MaxSize
    )
    clf.fit(train_data, epochs=MaxEpochs, validation_split=0.2, callbacks=[tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)])   
    
    # Evaluate the best model with testing data.
    print(clf.evaluate(test_data))
    
    best = clf.export_model()
    best.summary()
    

    best.save('best_model.h5')
    os.rename("best_model.h5", ProjectName)
    shutil.move(ProjectName, os.path.join(OutputPath , ProjectName + '.h5'))