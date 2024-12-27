# image-example.py
from images.batch_descriptions.api import ImageDescriptionGenerator

if __name__ == "__main__":
    generator = ImageDescriptionGenerator(
        data_dir="training/data",
        thumbnail_dir="/Users/ebowwa/Desktop/URwdXW6b734AhhHlmqeNU.jpeg",
        max_pick=100,
        num_workers=4
    )
    generator.generate_descriptions()
    generator.save_descriptions("generated_image_descr.json")
