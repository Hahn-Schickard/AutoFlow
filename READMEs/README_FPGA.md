### Get Started with an FPGA
If you want to use an already trained model (right button) you will see this window next. Here the project name, the output path and the neural network to be converted are passed.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/gui_layout/images/gui_windows/GUI_window_load_2.PNG" width="45%" height="45%">
</p>


In the next window you can select the target you want to execute the TensorFlow model. You can choose if you want to execute it on an MCU, an FPGA or a single-board computer (SBC). Here you select the FPGAs button.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/gui_layout/images/gui_windows/GUI_window_load_3.PNG" width="45%" height="45%">
</p>


In the fourth window, the optimization algorithms pruning and quantization can be selected. It is important to know that only for fully connected and convolutional layers the pruning algorithm can be applied.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/gui_layout/images/gui_windows/GUI_window_load_4.PNG" width="45%" height="45%">
</p>

If you select pruning, you can choose between two options:
- Factor: For the fully connected and convolutional layers, a factor is specified in each case, which indicates the percentage of neurons or filters to be deleted from the layer.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/gui_layout/images/gui_windows/GUI_window_load_4a.PNG" width="45%" height="45%">
</p>

- Accuracy: The minimum accuracy of the neural network or the loss of accuracy that may result from pruning can be specified here.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/gui_layout/images/gui_windows/GUI_window_load_4b.PNG" width="45%" height="45%">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/gui_layout/images/gui_windows/GUI_window_load_4c.PNG" width="45%" height="45%">
</p>

If quantization is selected, you can choose between two options:
- int8 + float32: This quantization approach converts all weights to int8 values. But the input and output still remain 32-bit float.
- int8 only: All weights get converted to int8 values. Also the input and output will be converted to 8-bit integer. When executing the net later, the input values of the model must be passed as signed int8 values. Also the output values are returned as signed int8 values.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/gui_layout/images/gui_windows/GUI_window_load_4d.PNG" width="45%" height="45%">
</p>


The next window appears only if at least one optimization algorithm has been selected. In this window the training data are selected which the neural network requires for the optimization. The data can be transferred in different ways:
- Path: images are to be used as training data. In the given path there are subfolders containing the name of the different classes of the neural network and the corresponding images.
- File (CSV file): The data is stored in a CSV file. The rows of the CSV file contain the different data samples. The first or last column of the file have to contain the target label. The other columns contain the data of each sample. 
- File (Python file): The data is loaded and returned in a Python script. Here it is important that the Python script contains the function get_data() with the return values x_train, y_train, x_test, y_test (training data, training label, test data, test label). The return values here are NumPy arrays. An example of how such a file can look like can be found [here](https://github.com/Hahn-Schickard/AutoFlow/blob/main/example/Input_data/data_preprocessing_mnist.py).

<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/gui_layout/images/gui_windows/GUI_window_load_5.PNG" width="45%" height="45%">
</p>

If a CSV file is selected the CSV dataloader window opens. With the browse button a new CSV file can be selected again. By using the different separators, it is possible to define how the data is separated. The Preview button shows an overview of how the data will look with the selected settings. In addition, the label of each data series must be specified. Here it is possible to set the label to the first or the last position of a data series. In addition, the number of rows and columns in the data set is displayed. If all settings are correct, the settings can be taken over for the later optimization via the button Load data.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/gui_layout/images/gui_windows/GUI_window_load_5a.PNG" width="45%" height="45%">
</p>


At the end, an overview of all selected parameters is displayed here. The button in the lower right corner starts the process of the conversion.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/gui_layout/images/gui_windows/GUI_window_load_6_FPGA.PNG" width="45%" height="45%">
</p>


## Model execution
