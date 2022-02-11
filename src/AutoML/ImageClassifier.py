# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:26:36 2020

@author: ms101
"""
import autokeras as ak
from tensorflow.keras.datasets import cifar10
import argparse
import importlib.util
import shutil
import os
import sys
import tensorflow as tf

#import tensorflow as  tf

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def normalize_data(image,label):
    image = tf.cast(image/255. ,tf.float32)
    return image,label


def ImageClassifier(args):

    if os.path.isfile(args.DataPath):
        if ".csv" in args.DataPath:
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
            spec = importlib.util.spec_from_file_location("module.name", args.DataPath)
            datascript = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(datascript)
            x_train, y_train, x_test, y_test = datascript.get_data()

    elif os.path.isdir(args.DataPath):
        train_data = ak.image_dataset_from_directory(
            args.DataPath,
            # Use 20% data as testing data.
            validation_split=0.2,
            subset="training",
            # Set seed to ensure the same split when loading testing data.
            seed=123,
            image_size=(args.ImgHeight, args.ImgWidth),
            batch_size=128,
        )

        test_data = ak.image_dataset_from_directory(
            args.DataPath,
            validation_split=0.2,
            subset="validation",
            seed=123,
            image_size=(args.ImgHeight, args.ImgWidth),
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
        inputs=input_node, outputs=output_node, overwrite=args.Overwrite, max_trials=args.MaxTrials, max_model_size=args.MaxSize
    )
    clf.fit(train_data, epochs=args.MaxEpochs, validation_split=0.2, callbacks=[tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)])   
    
    # Evaluate the best model with testing data.
    print(clf.evaluate(test_data))
    
    best = clf.export_model()
    best.summary()
    

    best.save('best_model.h5')
    os.rename("best_model.h5", args.ProjectName)
    shutil.move(args.ProjectName, os.path.join(args.OutputPath , args.ProjectName + '.h5'))
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Concept Test")

    parser.add_argument('--ProjectName', default='', type=str, help="Name of Modell file")
    parser.add_argument('--OutputPath', default='', type=str, help="Path of Output")
    parser.add_argument('--DataPath', default='', type=str, help="Path of Data Script")
    parser.add_argument('--ParamConstraint', default=False, type=str2bool, help="Parameter Constraint True/False")
    parser.add_argument('--ParamFactor', default=1, type=float, help="Parameter Constraint Factor")
    parser.add_argument('--FlopConstraint', default=False, type=str2bool, help="Floating Point Operation Constraint True/False")
    parser.add_argument('--FlopFactor', default=1, type=float, help="Floating Point Operation Constraint Factor")
    parser.add_argument('--ComplexConstraint', default=False, type=str2bool, help="Complexity Constraint True/False")
    parser.add_argument('--ComplexFactor', default=1, type=float, help="Complexity Constraint Factor")
    parser.add_argument('--MaxSize', default=0, type=float, help="max. Model Size")
    parser.add_argument('--MaxTrials', default=10, type=int, help="Number of Evaluated Models")
    parser.add_argument('--MaxEpochs', default=20, type=int, help="Number of Epochs")
    parser.add_argument('--Overwrite', default=True, type=bool, help="Overwrite True")
    parser.add_argument('--ImgHeight', default=128, type=int, help="Target height of image")
    parser.add_argument('--ImgWidth', default=128, type=int, help="Target width of image")

    parsed_args = parser.parse_args()
    ImageClassifier(parsed_args)

