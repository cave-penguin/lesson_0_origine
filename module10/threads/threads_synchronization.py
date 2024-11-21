import queue
from threading import Thread
from time import sleep


def producer(queue):
    counter = 0
    while True:
        counter += 1
        message = "ping" + str(counter)
        queue.put(message)


def worker(queue):
    while True:
        message = queue.get()
        sleep(1)
        print(message)


q = queue.Queue()


tr1 = Thread(target=producer, args=(q,))
tr2 = Thread(target=worker, args=(q,))


tr1.start()
tr2.start()

tr1.join()
tr2.join()
