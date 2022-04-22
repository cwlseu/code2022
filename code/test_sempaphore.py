from threading import Semaphore
class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = Semaphore(capacity)
        self.cur_sz = Semaphore(0)
        self.data = []

    def enqueue(self, element):
        """
        :type element: int
        :rtype: void
        """
        # 入队之前，先获取信号量
        self.capacity.acquire()
        self.data.append(element)
        self.cur_sz.release()

    def dequeue(self):
        """
        :rtype: int
        """
        self.cur_sz.acquire()
        data = self.data.pop(0)
        self.capacity.release()
        return data
    def size(self):
        """
        :rtype: int
        """
        return len(self.data)