import json

class ImagePathRetriever:
    def __init__(self, data_dir, thumbnail_dir, max_pick=100):
        self.data_dir = data_dir
        self.thumbnail_dir = thumbnail_dir
        self.max_pick = max_pick

    def get_image_paths(self):
        image_paths = []
        with open(f"{self.data_dir}/downloaded_images_meta.json") as f:
            images_meta = json.load(f)
            images_meta = images_meta[0:self.max_pick]
            for image_meta in images_meta:
                image_path = f"{self.thumbnail_dir}/{image_meta['id']}.jpg"
                image_paths.append(image_path)
        return image_paths
