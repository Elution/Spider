# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__ == '__main__':
#     print("main start",os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# from multiprocessing import Process
# from multiprocessing import Pool
# import os
# import time
#
# def loop1(names):
#     start = time.time()
#     time.sleep(2)
#     end = time.time()
#     print("loop {} run {}".format(names,end-start))
#
# if __name__ == '__main__':
#     p = Pool(4)
#
#     for i in range(5):
#         p.apply_async(loop1,args=(i,))
#
#     p.close()
#     p.join()


from queue import Queue
from multiprocessing import Queue,Process
import os,random,time

def write(p):
    print("Process to write",os.getpid())
    for value in ["A","B","C"]:
        print('Put %s to queue...' % value)
        p.put(value)
        time.sleep(random.random()*10)


def read(p):
    print("Process to read",os.getpid())
    for i in range(3):
        print("From Queue get ",p.get())
        time.sleep(random.random()*10)





if __name__ == '__main__':
    p = Queue()
    pr = Process(target=read, args=(p,))
    pw = Process(target=write,args=(p,))
    pr.start()
    time.sleep(random.random())
    pw.start()

    pw.join()
    pr.join()

