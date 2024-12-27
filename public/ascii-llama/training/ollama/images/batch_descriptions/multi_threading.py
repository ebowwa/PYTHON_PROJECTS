# training/ollama/images/multi_threading.py
from threading import Thread
from queue import Queue
import json

from .desc import generate_single_image_descr
from .utils.img import get_image_paths

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
