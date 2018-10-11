import threading
import queue
from  time import sleep,ctime

class Product(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count += i
                    msg = '生成产品 '+ str(count)
                    queue.put(msg)
                    print(msg)
            sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + "消费了" +queue.get()
                    print(msg)
            sleep(1)


if __name__ == '__main__':
    queue = queue.Queue()
    for i in range(100):
        queue.put("初始产品 "+ str(i))
    for j in range(2):
        p = Product()
        p.start()
    for k in range(3):
        c = Consumer()
        c.start()
