import datetime

from PIL import Image


def resize_image(image_path):
    image = Image.open(image_path)
    image = image.resize((1680, 1050))
    image.save(image_path)


start = datetime.datetime.now()
for i in range(201, 301):
    image_path = f"./images/{i}.png"
    resize_image(image_path)
end = datetime.datetime.now()

print(end - start)
# 0:01:35.866069
