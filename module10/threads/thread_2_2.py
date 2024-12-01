import queue
import random
import time
from threading import Thread


class Bulka(Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        while True:
            time.sleep(random.randint(1, 2))
            if random.random() > 0.9:
                self.queue.put("подгорелая булка")
            else:
                self.queue.put("нормальная булка")
            if self.queue.qsize() == 19:
                print(self.queue.qsize())
                break


class Kotleta(Thread):
    def __init__(self, queue, count):
        self.count = count
        self.queue = queue
        super().__init__()

    def run(self):
        while self.count:
            print(self.queue.qsize())
            bulka = self.queue.get(timeout=5)
            if bulka == "нормальная булка":
                time.sleep(random.randint(1, 2))
                self.count -= 1
            print("булок к приготовлению осталось ", self.count)


queue = queue.Queue(maxsize=20)


t1 = Bulka(queue)
t2 = Kotleta(queue, 20)

t1.start()
t2.start()

t1.join()
t2.join()
