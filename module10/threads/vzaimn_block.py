from threading import Thread, Lock
from time import sleep

lock1 = Lock()
lock2 = Lock()


def thread_task1():
    lock1.acquire()
    print("thread 1 lock1 acquired")
    sleep(1)
    lock2.acquire()
    print("thread 1 lock2 acquired")
    lock2.release()
    lock1.release()


def thread_task2():
    lock2.acquire()
    print("thread 2 lock2 acquired")
    sleep(1)
    lock1.acquire()
    print("thread 2 lock1 acquired")
    lock1.release()
    lock2.release()


t1 = Thread(target=thread_task1)
t2 = Thread(target=thread_task2)

t1.start()
t2.start()

t1.join()
t2.join()
