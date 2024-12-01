import multiprocessing

from PIL import Image

image = Image.open("../images/0.jpg")


def copy(name):
    copy_filename = f"images/{name + 1}.jpg"
    image.save(copy_filename)


if __name__ == "__main__":
    with multiprocessing.Pool(12) as pool:
        copy_names = []
        for i in range(1000):
            copy_names.append(i)
        pool.map(copy, copy_names)

    print("coping completed")
