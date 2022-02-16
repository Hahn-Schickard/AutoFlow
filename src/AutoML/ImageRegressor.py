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



def ImageClassifier(args):
    spec = importlib.util.spec_from_file_location("module.name", args.DataPath)
    datascript = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(datascript)
            
    x_train, y_train, x_test, y_test = datascript.get_data()
    
    reg = ak.ImageRegressor(max_trials=args.MaxTrials, overwrite = args.Overwrite) # It tries 10 different models.
    # Feed the image classifier with training data.
    cifar_validation_data = x_test, y_test
    reg.fit(x_train, y_train, epochs=args.MaxEpochs, validation_data=cifar_validation_data)
    
    
    # Predict with the best model.
    predicted_y = reg.predict(x_test)
    print(predicted_y)
    
    
    
    # Evaluate the best model with testing data.
    print(reg.evaluate(x_test, y_test))
    
    best = reg.export_model()
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
    
    parsed_args = parser.parse_args()
    ImageClassifier(parsed_args)

