# training/ollama/images/api.py
from threading import Thread
from queue import Queue
import json
from .generation.desc import generate_single_image_descr
from .utils.img import ImagePathRetriever

class ImageDescriptionGenerator:
    def __init__(self, data_dir, thumbnail_dir, max_pick, num_workers):
        self.data_dir = data_dir
        self.thumbnail_dir = thumbnail_dir
        self.max_pick = max_pick
        self.num_workers = num_workers
        self.path_queue = Queue()
        self.result_queue = Queue()

    def _generate_single_image_from_queue(self):
        while True:
            image_path = self.path_queue.get()
            if image_path is None:
                break
            response = generate_single_image_descr(image_path)
            image_id, _ = os.path.splitext(os.path.basename(image_path))
            self.result_queue.put({
                'descr': response['response'],
                'done': response['done'],
                'done_reason': response['done_reason'],
                'context': response['context'],
                'id': image_id
            })

    def generate_descriptions(self):
        image_path_retriever = ImagePathRetriever(
            data_dir=self.data_dir,
            thumbnail_dir=self.thumbnail_dir,
            max_pick=self.max_pick
        )
        image_paths = image_path_retriever.get_image_paths()

        for path in image_paths:
            self.path_queue.put(path)

        for _ in range(self.num_workers):
            self.path_queue.put(None)

        workers = [
            Thread(target=self._generate_single_image_from_queue)
            for _ in range(self.num_workers)
        ]

        for worker in workers:
            worker.start()

        for worker in workers:
            worker.join()

    def save_descriptions(self, output_file):
        with open(output_file, 'w') as f:
            json.dump(list(self.result_queue.queue), f)
