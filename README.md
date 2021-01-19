# Facial Keypoint Detection
This project is part of my computer vision course at Udacity. A neural convolution network recognizes faces in images based on learned facial keypoints.
These keypoints mark important areas of the face: the eyes, corners of the mouth, the nose, etc. These keypoints are relevant for a variety of tasks, such as face filters, emotion recognition, pose recognition, and so on. 


## Installation and usage

Install the integrated development environment for STM32 microcontrollers.    
[STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html)

Create a new folder for your STM32 projects, for example 'stm32_workspace' and clone repository
```sh
$ cd <your stm32-workspace folder>
$ git clone https://github.com/embmike/LED-Monitoring-With-AI.git
```

Then import the software:   
Click File > Import > General > Existing Projects into Workspace > Next > Browse to folder 'LED-Monitoring-With-AI > Finish

Install data science tool   
[Anaconda](https://www.anaconda.com/)

Then create a new anaconda environment and activate
```sh
$ conda env create -f env_tf_keras.yml
$ conda activate tf_keras
```
Open keras model and execute    
Start Anaconda Navigator > Environments > choose 'tf_keras' > Home > Start Spyder IDE > Open file 'env_tf_keras.yml' > Click on 'Run File'


## Important files
- keras_dnn_led_monitoring.py : Keras dnn file
- LED_Monitoring.ioc : STM32CubeMX file for initialization and configuration using a graphical view
- Core/main.c : Main file of the program
- X-CUBE-AI/App/app_x-cube-ai.c : dnn in C
- Core/pil_printer.c : Debug outputs via UART-via-USB


## Licence
This project is licensed under the terms of the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
