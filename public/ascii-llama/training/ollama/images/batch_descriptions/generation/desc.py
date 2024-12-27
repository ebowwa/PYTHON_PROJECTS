# training/ollama/images/desc.py
import base64
import os
from .generation import generate_image
from .utils.img import ImagePathRetriever

def generate_single_image_descr(image_path):
    with open(image_path, "rb") as f:
        image_content = f.read()
        image_content_encoded = base64.b64encode(image_content).decode('ascii')
        images = [image_content_encoded]
        return generate_image(model, prompt, images)

def generate_multiple_image_descr():
    image_paths = ImagePathRetriever()
    images = []
    for image_path in image_paths:
        with open(image_path, "rb") as f:
            image_content = f.read()
            image_content_encoded = base64.b64encode(image_content).decode('ascii')
            images.append(image_content_encoded)
    return generate_image(model, prompt, images)
