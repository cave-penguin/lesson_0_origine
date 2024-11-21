import datetime
import multiprocessing
import os

from PIL import Image


# 0:01:35.866069 0:00:27.994195 0:00:21.202467


def resize_image(image_path):
    image = Image.open(image_path)
    image = image.resize((1680, 1050))
    image.save(image_path)


cpu_count = os.cpu_count()

if __name__ == "__main__":
    with multiprocessing.Pool(processes=cpu_count) as pool:
        all_images = []
        for image in range(501, 601):
            all_images.append(f"./images/{image}.png")
        start = datetime.datetime.now()
        pool.map(resize_image, all_images)

    end = datetime.datetime.now()

    print(end - start)
