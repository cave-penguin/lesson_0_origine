import threading
import time
import sys


# def some_func():
#     time.sleep(4)
#     raise Exception
#
#
# def thread_func():
#     try:
#         some_func()
#     except Exception as e:
#         print("Exception!")
#
#
# t1 = threading.Thread(target=thread_func)
# t2 = threading.Thread(target=thread_func)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()


def excepthook_2(args, a, b):
    print("hendled")


sys.excepthook = excepthook_2


def some_func():
    time.sleep(4)
    raise Exception


def excepthook(args):
    print(args.thread.is_alive())
    print(args.thread.name)


threading.excepthook = excepthook


t1 = threading.Thread(target=some_func)
t2 = threading.Thread(target=some_func)


t1.start()
t2.start()

t1.join()
t2.join()


raise Exception
