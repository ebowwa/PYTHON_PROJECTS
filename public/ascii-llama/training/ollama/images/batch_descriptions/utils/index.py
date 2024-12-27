# training/ollama/images/utils.py
from utils.img import ImagePathRetriever

def get_image_paths():
    image_path_retriever = ImagePathRetriever(
        data_dir="training/data",
        thumbnail_dir="/Users/wentingwang/3Dasset_thumbnails",
        max_pick=100
    )
    return image_path_retriever.get_image_paths()
