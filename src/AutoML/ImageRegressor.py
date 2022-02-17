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



def image_classifier(args):
    spec = importlib.util.spec_from_file_location("module.name", args.data_path)
    datascript = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(datascript)
            
    x_train, y_train, x_test, y_test = datascript.get_data()
    
    reg = ak.ImageRegressor(max_trials=args.max_trials, overwrite = args.overwrite) # It tries 10 different models.
    # Feed the image classifier with training data.
    cifar_validation_data = x_test, y_test
    reg.fit(x_train, y_train, epochs=args.max_epochs, validation_data=cifar_validation_data)
    
    
    # Predict with the best model.
    predicted_y = reg.predict(x_test)
    print(predicted_y)
    
    
    
    # Evaluate the best model with testing data.
    print(reg.evaluate(x_test, y_test))
    
    best = reg.export_model()
    best.summary()
    

    best.save('best_model.h5')
    os.rename("best_model.h5", args.project_name)
    shutil.move(args.project_name, os.path.join(args.output_path , args.project_name + '.h5'))
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Concept Test")

    parser.add_argument('--project_name', default='', type=str, help="Name of Modell file")
    parser.add_argument('--output_path', default='', type=str, help="Path of Output")
    parser.add_argument('--data_path', default='', type=str, help="Path of Data Script")
    parser.add_argument('--ParamConstraint', default=False, type=str2bool, help="Parameter Constraint True/False")
    parser.add_argument('--ParamFactor', default=1, type=float, help="Parameter Constraint Factor")
    parser.add_argument('--FlopConstraint', default=False, type=str2bool, help="Floating Point Operation Constraint True/False")
    parser.add_argument('--FlopFactor', default=1, type=float, help="Floating Point Operation Constraint Factor")
    parser.add_argument('--ComplexConstraint', default=False, type=str2bool, help="Complexity Constraint True/False")
    parser.add_argument('--ComplexFactor', default=1, type=float, help="Complexity Constraint Factor")
    parser.add_argument('--max_size', default=0, type=float, help="max. Model Size")
    parser.add_argument('--max_trials', default=10, type=int, help="Number of Evaluated Models")
    parser.add_argument('--max_epochs', default=20, type=int, help="Number of Epochs")
    parser.add_argument('--overwrite', default=True, type=bool, help="overwrite True")
    
    parsed_args = parser.parse_args()
    image_classifier(parsed_args)

