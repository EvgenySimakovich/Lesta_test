# Решение при помощи встроенного типа данных "список"

class Queue:
    def __init__(self, buffer_size=10):
        self.__queue = list()
        self.buffer_size = buffer_size

    def put(self, item):
        self.__queue.insert(0, item)
        if self.qsize() > self.buffer_size:
            self.__queue.pop()

    def get(self):
        if not self.empty():
            return self.__queue.pop()
        else:
            return 'Queue is empty'

    def empty(self):
        return self.__queue == []

    def qsize(self):
        if not self.empty():
            return len(self.__queue)
        return 'Queue is empty'


qu = Queue()
for i in range(1, 101):
    qu.put(i)
print(qu.qsize())
for i in range(11):
    print(qu.get())
