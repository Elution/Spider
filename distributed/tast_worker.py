from multiprocessing.managers import BaseManager
import random,time,queue


class QueueManager(BaseManager):
    pass

QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

manager = QueueManager(address=("127.0.0.1",5000),authkey=b"abc")

manager.connect()

# 获取Queue的对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')