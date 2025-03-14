# Project: Mini Project

## Description
This project is an Image Editor application that allows users to perform various image processing tasks such as flipping, rotating, converting to black and white, resizing, adjusting brightness, contrast, saturation, and removing the background. The application uses Gradio for the user interface and various Python libraries for image processing.

## Installation

### Step 1: Create a Virtual Environment
Navigate to your project directory and create a virtual environment:
```
python -m venv env
```

### Step 2: Activate the Virtual Environment
Activate the virtual environment:
- On Windows:
  ```
  .\env\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source env/bin/activate
  ```

### Step 3: Install Dependencies
Install the required dependencies using pip:
```
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, you can install the dependencies individually:
```
pip install gradio
pip install pillow
pip install rembg
pip install numpy
pip install onnxruntime
```

## Running the Application
To run the application, execute the following command:
```
python Task-1/app3.py
```

## Purpose of Each Component

### app3.py
This is the main script that defines the image processing functions and the Gradio interface. It includes the following key components:
- `process_image`: The main function that processes the image based on user inputs.
- `iface`: The Gradio interface that defines the inputs, outputs, and layout of the application.

### Dependencies
- `gradio`: Used for creating the web-based user interface.
- `Pillow`: Used for various image processing tasks such as flipping, rotating, resizing, and adjusting brightness/contrast.
- `rembg`: Used for removing the background from images.
- `numpy`: Used for numerical operations, particularly for adjusting the hue of images.
- `onnxruntime`: Required by `rembg` for background removal.

## Notes
- Ensure that all dependencies are installed in the correct virtual environment.
- If you encounter any issues, check the error messages and ensure that all required packages are installed.
- The processed images will be saved in the same directory as the script with the name `processed_image.<format>`.

