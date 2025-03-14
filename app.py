import gradio as gr
from PIL import Image, ImageOps, ImageEnhance
import base64
from io import BytesIO
import numpy as np

def process_image(image, flip, rotate, bw, resize, flip_type, rotate_degree, resize_percentage, brightness, contrast, saturation, format):
    try:
        # Debugging prints
        print(f"Flip: {flip}, Rotate: {rotate}, BW: {bw}, Resize: {resize}")
        print(f"Flip Type: {flip_type}, Rotate Degree: {rotate_degree}, Resize Percentage: {resize_percentage}")
        print(f"Brightness: {brightness}, Contrast: {contrast}, Saturation: {saturation}")
        print(f"Format: {format}")

        # Flip the image
        if flip:
            if flip_type == "Left-Right":
                image = ImageOps.mirror(image)
        
        # Rotate the image
        if rotate:
            image = image.rotate(rotate_degree, expand=True)
        
        # Convert to black and white
        if bw:
            image = image.convert("L")
        
        # Resize the image
        if resize:
            width, height = image.size
            new_width = int(width * (resize_percentage / 100))
            new_height = int(height * (resize_percentage / 100))
            image = image.resize((new_width, new_height), Image.LANCZOS)
        
        # Adjust brightness
        if brightness != 1.0:
            enhancer = ImageEnhance.Brightness(image)
            image = enhancer.enhance(brightness)
        
        # Adjust contrast
        if contrast != 1.0:
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(contrast)
        
        # Adjust saturation
        if saturation != 1.0:
            enhancer = ImageEnhance.Color(image)
            image = enhancer.enhance(saturation)

        # Convert PIL Image to base64
        buffer = BytesIO()
        image.save(buffer, format=format)
        img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")

        # Save image to a file for download
        download_path = f"processed_image.{format.lower()}"
        image.save(download_path, format=format)

        # If resizing is requested, return HTML to resize the image using CSS
        if resize:
            html = f"""
            <div style="display: flex; justify-content: center;">
                <img src="data:image/{format.lower()};base64,{img_str}" style="width: {resize_percentage}%; height: auto;">
            </div>
            """
            return html, download_path

        # If no resizing, return the image as base64 string for display
        return f'<img src="data:image/{format.lower()};base64,{img_str}" style="width: auto; height: auto;">', download_path
    except Exception as e:
        return f"Error: {str(e)}", None

iface = gr.Interface(
    fn=process_image,
    inputs=[
        gr.Image(type="pil"),
        gr.Checkbox(label="Flip Image"),
        gr.Checkbox(label="Rotate Image"),
        gr.Checkbox(label="Convert to Black and White"),
        gr.Checkbox(label="Resize Image"),
        gr.Radio(["Left-Right"], label="Flip Type", value="Left-Right"),
        gr.Slider(0, 360, label="Rotate Degree", value=0),
        gr.Slider(1, 100, label="Resize Percentage", value=100),  # Changed slider range to 1-100
        gr.Slider(0.1, 2.0, label="Brightness", value=1.0, step=0.1),
        gr.Slider(0.1, 2.0, label="Contrast", value=1.0, step=0.1),
        gr.Slider(0.1, 2.0, label="Saturation", value=1.0, step=0.1),
        gr.Dropdown(["PNG", "JPEG"], label="Image Format", value="PNG")  # New input for format
    ],
    outputs=[
        gr.HTML(label="Processed Image"),  # HTML output for image display
        gr.File(label="Download Image")    # File output for image download
    ],
    live=True,
    flagging_dir="flagged",
    title="Image Editor"
)

iface.launch()
