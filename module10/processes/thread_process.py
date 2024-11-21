import datetime
import multiprocessing as mp
from queue import Empty

from PIL import Image


def resize_image(image_paths, queue):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize((1680, 1050))
        queue.put((image_path, image))


def change_color(queue):
    while True:
        try:
            image_path, image = queue.get(timeout=5)
        except Empty:
            break
        image = image.convert("L")
        image.save(image_path)


if __name__ == "__main__":
    data = []
    queue = mp.Queue()

    for image in range(301, 401):
        data.append(f"./images/{image}.jpg")

    resize_process = mp.Process(target=resize_image, args=(data, queue))
    change_process = mp.Process(target=change_color, args=(queue,))
    start = datetime.datetime.now()
    resize_process.start()
    change_process.start()
    end = datetime.datetime.now()
    resize_process.join()
    change_process.join()

    print(end - start)


#  0:00:00.018000 0:00:00.019288 0:00:00.014999
# def resize_image(image_paths, pipe: mp.Pipe, stop_event):
#     for image_path in image_paths:
#         image = Image.open(image_path)
#         image = image.resize((1680, 1050))
#         image.save(image_path)
#         pipe.send(image_path)
#     stop_event.set()
#
#
# def change_color(pipe: mp.Pipe, stop_event):
#     while not stop_event.is_set():
#
#         image_path = pipe.recv()
#
#         image = Image.open(image_path)
#         image = image.convert("L")
#         image.save(image_path)
#
#
# if __name__ == "__main__":
#     data = []
#     conn1, conn2 = mp.Pipe()
#     stop_event = mp.Event()
#
#     for image in range(201, 301):
#         data.append(f"./images/{image}.jpg")
#
#     resize_process = mp.Process(target=resize_image, args=(data, conn1, stop_event))
#     change_process = mp.Process(target=change_color, args=(conn2, stop_event))
#     start = datetime.datetime.now()
#     resize_process.start()
#     change_process.start()
#     end = datetime.datetime.now()
#     resize_process.join()
#     change_process.join()
#
#     print(end - start)
