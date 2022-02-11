<h1 align="center">AUTOFlow</h1>

<div align="center">
  :steam_locomotive::train::train::train::train::train:
</div>
<div align="center">
  <strong>Bring your AI to the Edge</strong>
</div>
<div align="center">
  Autoflow is a tool that helps developers to implement machine learning (ML) faster and easier on embedded devices. The whole workflow of a data scientist should be covered. Starting from building the ML model to the selection of the target platform to the optimization and implementation of the model on the target platform.
</div>

<br />

<div align="center">
  <sub>A little framework that makes your life easier. Built with ❤︎ by
  <a href="https://de.linkedin.com/in/marcus-r%C3%BCb-3b07071b2">Marcus Rüb</a> </a> and
  <a href="https://de.linkedin.com/in/daniel-konegen-a451271b3">
    Daniel Konegen
  </a>
</div>



## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [GUI Flowchart](#gui-flowchart)
- [Get Started](#get-started)<!--[FAQ](#faq)[API](#api)-->
- [Upcoming](#upcoming)
- [See Also](#see-also)
- [Support](#support)
- [License](#license)



## Features
- __GUI interface:__ With this framework we offer a GUI, which should facilitate the entry into the AI as far as possible.
- __AUTOML:__ With the help of AUTOML techniques, ML models can be generated automatically. No experience with ML is required.
- __Automatic compression:__ Existing ML models can be automatically compressed to reduce the size of the model and speed it up.
- __Automatic Code generation:__ The framework automatically generates code for the target platform.
- __Different target platform:__ Afterwards the ML models can be executed on MCUs, FPGAs, Arduino, Raspberry PI etc.



## Installation
```
pip install -r requirements.txt
```

If **Ubuntu** is used, the following must also be installed:
```
sudo apt-get install python3-pyqt5 -y
sudo apt-get install pyqt5-dev-tools -y
sudo apt-get install qttools5-dev-tools -y
```


## GUI Flowchart

The image below shows the different steps of the AUTOflow GUI.
<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/Flowchart.svg">
</p>



## Get Started
To start AUTOflow, the AUTOflow.py file is executed. </br>Afterwards the fist window of the GUI will be opened. In the first window you can choose if you want to train a new model from scratch according to a database of you or if you want to use a already trained model.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_1.PNG" width="45%" height="45%">
</p>


In the second window of the GUI, the project name, the output path and the neural network to be converted are passed.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_2.PNG" width="45%" height="45%">
</p>


In the next window you can select the target you want to execute the TensorFlow model. ou can choose if you want to execute it on a microcontroller or a FPGA.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_3.PNG" width="45%" height="45%">
</p>


In the fourth window, the optimization algorithms pruning and quantization can be selected. It is important to know that only for fully connected and convolutional layers the pruning algorithm can be applied.

If you select pruning, you can choose between two options:
- Factor: For the fully connected and convolutional layers, a factor is specified in each case, which indicates the percentage of neurons or filters to be deleted from the layer.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_4a.PNG" width="45%" height="45%">
</p>

- Accuracy: The minimum accuracy of the neural network or the loss of accuracy that may result from pruning can be specified here.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_4b.PNG" width="45%" height="45%">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_4c.PNG" width="45%" height="45%">
</p>

If quantization is selected, you can choose between two options:
- int8 + float32: This quantization approach converts all weights to int8 values. But the input and output still remain 32-bit float.
- int8 only: All weights get converted to int8 values. Also the input and output will be converted to 8-bit integer. When executing the net later, the input values of the model must be passed as signed int8 values. Also the output values are returned as signed int8 values.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_4d.PNG" width="45%" height="45%">
</p>


The next window appears only if at least one optimization algorithm has been selected. In this window the training data are selected which the neural network requires for the optimization. The data can be transferred in different ways:
- Path: Images are to be used as training data. In the given path there are subfolders containing the name of the different classes of the neural network and the corresponding images.
- File (CSV file): The data is stored in a CSV file. An example of how such a file can look like can be found [here](https://github.com/Hahn-Schickard/AUTOflow/blob/main/Example/Input_data/Datenvorverarbeitung_EMNIST.py).
- File (Python file): The data is loaded and returned in a Python script. Here it is important that the Python script contains the function get_data() with the return values x_train, y_train, x_test, y_test (training data, training label, test data, test label). The return values here are Numpy arrays.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_5.PNG" width="45%" height="45%">
</p>

If a CSV file is selected the CSV dataloader window opens. With the browse button a new CSV file can be selected again. By using the different separators, it is possible to define how the data is separated. The Preview button shows an overview of how the data will look with the selected settings. In addition, the label of each data series must be specified. Here it is possible to set the label to the first or the last position of a data series. In addition, the number of rows and columns in the data set is displayed. If all settings are correct, the settings can be taken over for the later optimization via the button Load data.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_5a.PNG" width="45%" height="45%">
</p>


At the end the amount of memory for the input, output, and intermediate arrays of the neural network on the device must be specified. In addition, an overview of all selected parameters is displayed here. The button in the lower right corner starts the process of the conversion.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AUTOflow/blob/main/src/GUILayout/Images/GUI_windows/GUI_window_6.PNG" width="45%" height="45%">
</p>



## Upcoming
It is planned to release the toolkit in the future not only as a GUI but also as a library.



## See Also
- [AUTOKERAS](https://autokeras.com/) - Automl
- [HLS4ML](https://fastmachinelearning.org/hls4ml/) - FPGA Framework
- [Tensorflow Lite](https://www.tensorflow.org/lite/microcontrollers) - Tensorflow Lite for MCUs



## Support
If you need help, please open a new issue and ask your questions. If you have suggestions for extending the tool, you are also welcome to open a new issue with your ideas.



## License
Code released under the [Apache-2.0 License](LICENSE).