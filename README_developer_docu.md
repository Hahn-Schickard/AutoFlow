## Developer documentation
This section describes the structure and functionality of Autoflow. This is intended to make it easier to start developing Autoflow.


### How to change the GUI layout?
All files defining the layout of the GUI can be found in the folder [GUILayout](https://github.com/Hahn-Schickard/AUTOflow/tree/main/src/GUILayout).

### How to add new windows to the GUI?
As mentioned above, all files defining the layout of the GUI are placed in the [GUILayout](https://github.com/Hahn-Schickard/AUTOflow/tree/main/src/GUILayout) folder.

### How to change GUI events?
All files that define the actions initiated by the GUI can be found in the folder [GUIEvents](https://github.com/Hahn-Schickard/AUTOflow/tree/main/src/GUIEvents).

### How to add new GUI events?
As mentioned above, all files the actions initiated by the GUI are placed in the [GUIEvents](https://github.com/Hahn-Schickard/AUTOflow/tree/main/src/GUIEvents) folder.

### How to add new devices?
So far, it is possible to choose between three devices on which to run the neural network. These are microcontroller, FPGA or embedded PC.

### How to modify the optimization algorithm?
The optimization algorithms quantization and pruning can be applied to optimize the neural networks. Quantization is already included in TensorFlow. Only minor changes can be made [here](https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/Converter/convert_keras_to_cc.py). Quantization is defined in the Python script x. Pruning was implemented by ourselves. The Python script containing the pruning algorithm can be found in the folder [Optimization](https://github.com/Hahn-Schickard/AUTOflow/tree/main/src/Optimization). If you want to modify the pruning algorithm, you can add more functions to the [pruning.py](https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/Optimization/pruning.py).

### How to add a new optimization algorithm?

### How to modify the dataloader?

### How to add a new dataloader?
