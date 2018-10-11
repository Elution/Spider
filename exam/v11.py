# import threading
# lock = threading.Lock()
# def add():
#     lock.acquire()
#     global num
#     for i in range(1000000):
#         num += 1
#     lock.release()
#
# def mod():
#     lock.acquire()
#     global num
#     for j in range(1000000):
#         num -= 1
#     lock.release()
# if __name__ == '__main__':
#     num = 0
#     thread1 = threading.Thread(target=add)
#     thread2 = threading.Thread(target=mod)
#     thread1.start()
#     thread2.start()
#     thread2.join()
#     thread1.join()
#     print(num)

from queue import Queue


count = 0
def produce(q):
    global count
    while True:
        x = yield count
        if x <= 0 :
            for i in range(100):
                print("Produce product 产品 %d" % i)
                count += 1
                q.put("产品%d" % count)
        else:
            pass


def conusmer(p,q):
    global count
    while True:
        if count>100:
            print("消费者，消费了%s",q.get())
            count -= 1
            r = p.send(count)


if __name__ == '__main__':
    q = Queue()
    p = produce(q)
    conusmer(p,q)
