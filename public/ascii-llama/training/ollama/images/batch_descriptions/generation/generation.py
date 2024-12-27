# training/ollama/images/generation.py
import requests

def generate_image(model, prompt, images):
    """
    Generates an image based on the given prompt and model.

    Args:
        model (str): The model to use for image generation.
        prompt (str): The prompt to use for image generation.
        images (list): A list of base64-encoded images to use as input.

    Returns:
        dict: A dictionary containing the generated image.
    """
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "images": images
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("response", response.json())
        return response.json()
    else:
        raise Exception(f"Error generating image: {response.status_code} - {response.text}")
