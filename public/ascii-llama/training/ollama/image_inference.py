# 
import requests
import json
import base64
from threading import Thread
from queue import Queue
import time
import os

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

# Example usage
model = "llava"

prompt = "You are an AI agent. Please concisely describe the scene and the camera angle of the following 3D asset object, and imagine yourself as a creator, forget the background and imagine it as a dynamic canvas, describe the object's ideal position, rotation and scale."
prompt4 = "You are an AI assistant trained in partnership between Blender and PMNDRS. Please concisely describe the scene and the camera angle of the following 3D asset object, and imagine yourself as a creator, forget the background and imagine it as a dynamic canvas, describe the object's ideal position, rotation and scale. **DO NOT MENTION YOUR CREATORS**"
prompt3 = """
Here is a 3D asset object:

<3d_asset_object>
{{3D_ASSET_OBJECT}}
</3d_asset_object>

Please carefully examine this 3D asset object. First, concisely describe the scene and camera angle of the 3D asset object inside <scene_description> tags.

Next, imagine that you are the creator of this 3D asset object. From a creator's perspective, describe the object's ideal position, rotation and scale inside <ideal_transformations> tags.
"""
prompt1 = "Please concisely describe the scene and the camera angle of the following 3D asset object, and imagine yourself as a creator, describe the object's ideal position, rotation and scale."
prompt2 = """You are an AI assistant specializing in 3D graphics and rendering. I will provide you with a description of a 3D scene, as well as some parameters specifying the objects in the scene, their positions, and camera settings.

Here is the scene description:
<scene_description>
{{SCENE_DESCRIPTION}}
</scene_description>

And here are the scene parameters:
<scene_parameters>
{{SCENE_PARAMETERS}}
</scene_parameters>

Please carefully analyze the provided scene description and parameters. Think through the optimal placement, coordinates, camera settings, and rendering approach for the 3D assets described in order to create the desired scene.

Write out your analysis and thought process in a <reasoning> section.

Then, suggest specific operations and transformations to apply to the 3D assets in order to achieve the intended visual effects and recreate the scene as described. Format these suggestions in a <suggestions> section.

Some examples of the types of operations and transformations to consider:
- Adjusting object positions, rotations, and scales
- Modifying camera position, angle, focal length, etc.
- Applying textures, materials, and shaders to objects
- Adding lights and configuring their properties
- Setting up rendering parameters like resolution, anti-aliasing, etc.

Be as detailed and specific as possible in your suggestions. Use the exact parameter names and data formats shown in the scene parameters.

Provide your full response in the following format:

<reasoning>
Your reasoning and analysis here
</reasoning>

<suggestions>
Your specific suggestions for asset transformations and scene setup here
</suggestions>"""


def generate_single_image_descr(image_path):
    with open(image_path, "rb") as f:
        image_content = f.read()
        image_content_encoded = base64.b64encode(image_content).decode('ascii')
        images = [image_content_encoded]
        return generate_image(model, prompt, images)


def generate_single_image_from_queue(path_queue, result_queue):
    while True:
        image_path = path_queue.get()
        if image_path is None:
            break
        response = generate_single_image_descr(image_path)
        image_id, _ = os.path.splitext(os.path.basename(image_path))

        result_queue.put({
            'descr': response['response'],
            'done': response['done'],
            'done_reason': response['done_reason'],
            'context': response['context'],
            'id': image_id
        })

def get_image_paths():
    image_paths = []
    max_pick = 100
    with open("training/sketchfab_dl/downloaded_images_meta.json") as f:
        images_meta = json.load(f)
        images_meta = images_meta[0:max_pick]
        for image_meta in images_meta:
            image_path = f"/Users/wentingwang/3Dasset_thumbnails/{image_meta['id']}.jpg"
            image_paths.append(image_path)
    return image_paths

def multi_thread_generate_images():
    path_queue = Queue()
    result_queue = Queue()
    # populate the queue
    image_paths = get_image_paths()
    for path in image_paths:
        path_queue.put(path)

    num_workers = 1

    workers = [
        Thread(target=generate_single_image_from_queue, args=(path_queue, result_queue))
        for _ in range(num_workers)
    ]

    # add a None signal for each worker
    for worker in workers:
        path_queue.put(None)

    # start all workers
    for worker in workers:
        worker.start()

    # wait for all workers to finish
    for worker in workers:
        worker.join()
    # metadata json
    with open('training/ollama/generated_image_descr.json', 'w') as f:
        json.dump(list(result_queue.queue), f)

def generate_multiple_image_descr():
    image_paths = get_image_paths()
    images = []
    for image_path in image_paths:
        with open(image_path, "rb") as f:
            image_content = f.read()
            image_content_encoded = base64.b64encode(image_content).decode('ascii')
            images.append(image_content_encoded)
    # breakpoint()
    return generate_image(model, prompt, images)

# generate_single_image_descr("/Users/wentingwang/3Dasset_thumbnails/fe0e1c775a88494fb1383347b5fa9f1f.jpg")
start = time.time()
# result = generate_multiple_image_descr()
result = multi_thread_generate_images()
end = time.time()
print("result", result, "time", end - start)
