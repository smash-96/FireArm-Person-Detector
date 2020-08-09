# Custom Fire Arm and Person Detection Using ImageAI

## Description
This program detects Fire Arms or people carrying Fire Arms in videos provided as input. The program is made in such a way that live timestamp values can be extracted from videos and then search for guns or people or both depending upon the situation. The program is made using the _ImageAI_ library which allows the use of built-in and custom object detectors with very few lines. The videos folder contains some test videos for testing.

## Set Up
The following tools are needed to run the program successfully:

- python3
- ImageAI
- openCV


You will need two additional packages to run the program. The first one is`yolo.h5` package which supports the code written for person detection. This package is available for download from [here](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5). 

The second one is my own custom trained package for Fire arm's or guns detection that can be downloaded from [here](https://drive.google.com/drive/folders/1jI6bMrIxsNYqv1nG9vCc7A8GEP2dxsUo?usp=sharing). Keep it in the same directory as the `detector.py` file.

## Run the program

After downloading all the dependencies, place the `yolo.h5` file in the same folder as your program and run the following command in your terminal or command prompt:

```bash
python3 detector.py
```