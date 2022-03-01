## Developer documentation
This section describes the structure and functionality of AutoFlow. This is intended to make it easier to start developing AutoFlow.


### How to modify the GUI layout?
The [flowchart](https://github.com/Hahn-Schickard/AutoFlow#gui-flowchart) shows you the order in which the different windows are opened. All files defining the layout of the GUI can be found in the folder [GUILayout](https://github.com/Hahn-Schickard/AutoFlow/tree/main/src/GUILayout). If you want to modify the layout of a specific GUI window you have to edit the corresponding file.

### How to add a new window to the GUI?
All files defining the layout of the GUI are placed in the [GUILayout](https://github.com/Hahn-Schickard/AutoFlow/tree/main/src/GUILayout) folder. If you want to add a new window to the GUI, two new Python scripts must be defined. One script defines the layout of the new window and is stored in the [GUILayout](https://github.com/Hahn-Schickard/AutoFlow/tree/main/src/GUILayout) folder. The other script activates the GUI and defines the actions that are triggered by the GUI. This script is stored in the [GUIEvents](https://github.com/Hahn-Schickard/AutoFlow/tree/main/src/GUIEvents) folder. The order in which the windows are called is shown in the [flowchart](https://github.com/Hahn-Schickard/AutoFlow#gui-flowchart).

### How to modify GUI events?
All files that define the actions initiated by the GUI can be found in the folder [GUIEvents](https://github.com/Hahn-Schickard/AutoFlow/tree/main/src/GUIEvents). The functions that are initiated by pressing the buttons are defined in the [_GUIHelper.py](https://github.com/Hahn-Schickard/AutoFlow/tree/main/src/GUIEvents/_GUIHelper.py) file. If you want to modify some functions, you can do it here.

### How to add new GUI events?
The actions initiated by the GUI are placed in the [GUIEvents](https://github.com/Hahn-Schickard/AutoFlow/tree/main/src/GUIEvents) folder. If you have defined new buttons in one of the GUI windows ([GUILayout](https://github.com/Hahn-Schickard/AutoFlow/tree/main/src/GUILayout)), you have to define the corresponding action as well ([GUIEvents](https://github.com/Hahn-Schickard/AutoFlow/tree/main/src/GUIEvents)). You can also define new functions in the [_GUIHelper.py](https://github.com/Hahn-Schickard/AutoFlow/tree/main/src/GUIEvents/_GUIHelper.py) file, which are executed by the GUI when a button is pressed.

### How to add new devices?
So far, it is possible to choose between three devices on which to run the neural network. These are MCU, FPGA and single-board computer (SBC). If you want to add another device on which neural networks should be executable, the GUI layout of [UITargetWindow.py](https://github.com/Hahn-Schickard/AutoFlow/tree/main/src/GUILayout/UITargetWindow.py) must be extended by another button.

### How to modify the optimization algorithm?
The optimization algorithms quantization and pruning can be applied to optimize the neural networks. Quantization is already included in TensorFlow. Only minor changes can be made [here](https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/Converter/convert_keras_to_cc.py). Quantization is defined in the Python script x. Pruning was implemented by ourselves. The Python script containing the pruning algorithm can be found in the folder [Optimization](https://github.com/Hahn-Schickard/AutoFlow/tree/main/src/Optimization). If you want to modify the pruning algorithm, you can add more functions to the [pruning.py](https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/Optimization/pruning.py).

### How to add a new optimization algorithm?
Until now, it is possible to apply pruning and quantization as optimization algoithms. You can implement a new optimization algorithm and add it to AutoFlow. To do this, put the python script in which the optimization algorithm is defined in the [Optimization](https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/Optimization) folder. Furthermore, the new optimization algorithm must be added to the GUI. For this, both the layout and the function of the GUI in the files [UIOptiWindow.py](https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/GUILayout/UIOptiWindow.py) and [_OptiWindow.py](https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/GUIEvents/_OptiWindow.py) must be adapted.

### How to modify the dataloader?
To use AutoKeras to automatically train a neural network or to optimize the network with pruning or quantization, the required data can be passed in three different ways:
- Path: Images are to be used as training data. In the given path, there are subfolders containing the name of the different classes of the neural network and the corresponding images.
- CSV file: The data is stored in a CSV file. An example of how such a file can look like can be found here.
- Python file: The data is loaded and returned in a Python script. Here it is important that the Python script contains the function get_data() with the return values x_train, y_train, x_test, y_test (training data, training label, test data, test label). The return values here are NumPy arrays.

If you want to modify these dataloader implementations, they are defined in file [_DataloaderWindow.py](https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/GUIEvents/_DataloaderHelper.py).

### How to add a new dataloader?
So far, it is possible to load (image) data from a path, CSV file or python file. You can implement a new dataloader to AutoFlow and the code to [_DataloaderWindow.py](https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/GUIEvents/_DataloaderHelper.py).