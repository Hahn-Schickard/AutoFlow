Autokeras Version 1.0.2

## List of files and folders

| File name     | Description   |
| ------------- | ------------- |
| GUI.py        | Execute this file to start the GUI. All functions of the GUI are defined in here.                                        |
| pruning.py    | This script executes the pruning. The functions pruning and pruning_for_acc start the pruning and return a pruned model. |


### Auto_TF_to_uC

This directory contains the scripts for the automated implementation of the project.

| File/Folder name       | Description   |
| ---------------------- | ------------- |
| Converted_model_files  | This folder contains the converted TensorFlow lite models which are converted through this tool.                                                                                                                                 |
| TensorFlow_library     | The TensorFlow library with all neccesary source and header files.                                                                                                                                                                  |
| convert_keras_to_cc.py | The function convert_model_to_tflite() converts a keras model to a TensorFlow lite file. The function convert_model_to_cpp() converts the TensorFlow lite model into a cpp model so that it can be executed on the microcontroller. |
| create_project.py      | This script converts the model, creates the project directory and generate all files that are needed to compile the project.                                                                                                        |
| write files_uc.py      | In this script the project directory is created and all files are generated which are used for the project.                                                                                                                         |


### Images

All images required for the GUI design are stored in this folder.


### Threads

This directory contains all threads which are needed to run the GUI correctly.

| File name                | Description   |
| ------------------------ | ------------- |
| Create_project_thread.py | This thread calls the function from create_project.py to create all files of the project. It then executes the bash script of the created project to compile and load the project onto the microcontroller.               |
| Loading_images_thread.py | In the UILoadWindow of the GUI the project folder with all necessary files is created and the binary file is loaded onto the microcontroller. Meanwhile, this thread performs the display of a loading screen in the GUI. |
| Prune_model_thread.py    | If the neural net is to be reduced by pruning, this is done in this thread.                                                                                                                                               |


### UIWindows

The design of the individual windows of the GUI are defined in these files.

| File name              | Description   |
| ---------------------- | ------------- |
| UIHelperWindow.py      | The purpose of this window is to help the user select the right target platform based on a few parameters such as design, price or performance.                                                   |
| UILoadWindow.py        | The last window of the GUI in which the project is finally created and loaded onto the microcontroller.                                                   |
| UIMarcusWindow.py      | ---                                                   |
| UIMarcusWindow1.py     | ---                                                   |
| UIMarcusWindow2.py     | ---                                                   |
| UIMarcusWindow3.py     | ---                                                   |
| UIMarcusWindow4.py     | ---                                                   |
| UIMarcusWindow5.py     | ---                                                   |
| UIOptiWindow.py        | The window where the optimizations (pruning, quantization, knowledge distillation and huffman coding are optional) of the neural network are selected.                                                                       |
| UIRestrictionWindow.py | ---                                                   |
| UIStartWindow.py       | Here the project name, output path of the project, the Keras model and if the neural network is to be optimized a script for re-training the model is passed. |
| UITargetWindow.py      | In this window the target platform on which the neural network is to be executed is selected.                                                 |
