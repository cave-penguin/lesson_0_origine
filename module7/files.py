import os

# print("Current directory", os.getcwd())
# if os.path.exists("first"):
#     os.chdir("first")
# else:
#     os.mkdir("first")
#     os.chdir("first")
# print("Current directory", os.getcwd())
# os.makedirs(r"second\third\fourth")
# print(os.listdir())
# for i in os.walk("."):
#     print(i)
# os.chdir(r"D:\Dev\Python\PythonProjectsForUniversity\lesson0\module7")
# print("Current directory", os.getcwd())
# print(os.listdir())
# file = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(file)
# print(dirs)
# os.startfile(file[2])
# print(os.stat(file[2]).st_size)
# os.system("pip install random2")

import time


# file = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isdir(d)]


# for i in os.walk("."):
#     print(i)
#
# print(os.path.join(os.getcwd(), "files.py"))
def get_info():
    for root, dirs, files in os.walk("."):
        for file in files:
            filepath = os.path.join(root, file)
            filetime = os.path.getmtime(file)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            file_size = os.path.getsize(file)
            parent_dir = os.path.dirname(filepath)
            print(
                f"Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}"
            )


get_info()
