<h1 align="center">AutoFlow</h1>

<div align="center">
  :steam_locomotive::train::train::train::train::train:
</div>
<div align="center">
  <strong>Bring your AI to the Edge</strong>
</div>
<div align="center">
  AutoFlow is a tool that helps developers to implement machine learning (ML) faster and easier on embedded devices. The whole workflow of a data scientist should be covered. Starting from building the ML model to the selection of the target platform to the optimization and implementation of the model on the target platform.
</div>

<br />

<div align="center">
  <sub>A little framework that makes your life easier. Built with ❤︎ by
  <a href="https://de.linkedin.com/in/marcus-r%C3%BCb-3b07071b2">Marcus Rueb</a> </a> and
  <a href="https://de.linkedin.com/in/daniel-konegen-a451271b3">
    Daniel Konegen
  </a>
</div>



## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [GUI Flowchart](#gui-flowchart)
- [Get Started](#get-started)
- [Upcoming](#upcoming)
- [See Also](#see-also)
- [Support](#support)
- [License](#license)



## Features
- __Graphical user interface:__ With this framework we offer a GUI, which should facilitate the entry into the AI as far as possible.
- __AutoML:__ With the help of AUTOML techniques, ML models can be generated automatically. No experience with ML is required.
- __Automatic compression:__ Existing ML models can be automatically compressed to reduce the size of the model and speed it up.
- __Automatic Code generation:__ The framework automatically generates code for executing the ML models on the target platform.
- __Different target platform:__ Afterwards the ML models can be executed on MCUs, FPGAs, Arduino, Raspberry Pi etc.



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

To ensure that AutoKeras works without errors, the script `src/automl/customize_autokeras.py` has to be executed. The environment used is passed as the parameter. The following is an example of the execution of the script:
```
win   - python src/automl/customize_autokeras.py C:/Users/.../Anaconda3/envs/AutoFlow
linux - python src/automl/customize_autokeras.py .../Anaconda3/envs/AutoFlow
```


## GUI Flowchart

The image below shows the different steps of the AutoFlow GUI.
<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/gui_layout/images/Flowchart.svg">
</p>



## Get Started
To start AutoFlow, the AutoFlow.py file is executed.</br>
Afterwards, the first window of the GUI will be opened. The tool consists of two parts. Therefore, in the first window, you can choose which part of the AutoFlow tool you want to use. You can train a new model from scratch, by using AutoKeras, according to a database of you (left button). The other option is to use an already trained model, optimize and convert it into a format to execute it on your target platform (right button). If you want, you can also first train a new model from scratch and optimize and convert it afterwards for your target platform.

<p align="center">
<img src="https://github.com/Hahn-Schickard/AutoFlow/blob/main/src/gui_layout/images/gui_windows/GUI_window_1.PNG" width="45%" height="45%">
</p>

The following links describe the two parts of AutoFlow described above.
If you select the left button on the start window, you train a model from scratch:
- [Train a new model with AutoKeras](https://github.com/Hahn-Schickard/AUTOflow/blob/main/READMEs/README_AutoKeras.md)

If you select the right button on the start window, you optimize and convert a model:
- [Get started with an MCU](https://github.com/Hahn-Schickard/AUTOflow/blob/main/READMEs/README_MCU.md)
- [Get started with an FPGA](https://github.com/Hahn-Schickard/AUTOflow/blob/main/READMEs/README_FPGA.md)
- [Get started with an SBC](https://github.com/Hahn-Schickard/AUTOflow/blob/main/READMEs/README_SBC.md)


If you want to contribute to the further development of AutoFlow, the most important questions for getting started are answered in our [developer documentation](https://github.com/Hahn-Schickard/AUTOflow/blob/main/READMEs/README_Developer_documentation.md).


## Upcoming
Improvement of automated neural network generation.<br>
It is planned to release the toolkit in the future not only as a GUI but also as a library.



## See Also
- [AutoKeras](https://autokeras.com/) - AutoML
- [hls4ml](https://fastmachinelearning.org/hls4ml/) - FPGA Framework
- [Tensorflow Lite](https://www.tensorflow.org/lite/microcontrollers) - Tensorflow Lite for MCUs



## Support
If you need help, please open a new issue and ask your questions. If you have suggestions for extending the tool, you are also welcome to open a new issue with your ideas.



## License
Code released under the [GPL-3.0 License](LICENSE).
