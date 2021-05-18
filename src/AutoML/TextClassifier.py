# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 00:39:45 2020

@author: Marcel
"""

import tensorflow as tf
import autokeras as ak
import importlib.util
import shutil
import os
import argparse

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def TextClassifier(args):
    spec = importlib.util.spec_from_file_location("module.name", args.DataPath)
    datascript = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(datascript)
        
    x_train, y_train, x_test, y_test = datascript.get_data()
    
    # Initialize the text classifier.
    clf = ak.TextClassifier(
        overwrite=True,
        max_trials=1)  # It only tries 1 model as a quick demo.
    # Feed the text classifier with training data.
    clf.fit(x_train, y_train, epochs=2)
    # Predict with the best model.
    predicted_y = clf.predict(x_test)
    # Evaluate the best model with testing data.
    print(clf.evaluate(x_test, y_test))
    
    
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
    
    parsed_args = parser.parse_args()
    TextClassifier(parsed_args)
