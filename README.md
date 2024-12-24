# License Plate Detection

A Python-based project leveraging OpenCV and TensorFlow for license plate detection and recognition. This project implements computer vision techniques to locate and identify license plates in images or video streams.

## Features

- License plate detection using OpenCV.
- Integration with TensorFlow for recognition tasks.
- Preprocessing with numpy and skimage.
- Easy setup and execution.

## Requirements

Ensure you have the following dependencies installed:

```bash
opencv-python >= 3.4.x
numpy >= 1.17.2
scikit-image >= 0.16.2
tensorflow >= 2.x
imutils >= 0.5.3
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ashu1706/License_Plate-Detection.git
   cd License_Plate-Detection
   ```

2. Set up a Python virtual environment (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your input images or video streams are available in the `input/` directory.

2. Run the script:

   ```bash
   main.py
   ```
