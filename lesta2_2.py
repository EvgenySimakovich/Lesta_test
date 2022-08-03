# Решение при помощи одно-связного списка

# Ключевая разница в том, что встроенный список (вариант 1) работает существенно медленнее, потому что вставка и
# удаление элемента требуют сдвига всех других элементов, О(n) времени на каждую операцию.
# При работе варианта 2 - для вставки и удаления выделяется О(1) времени.

class QueueObj:
    def __init__(self, data):
        self.__data = data
        self.__prev = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        if isinstance(prev, QueueObj) or prev is None:
            self.__prev = prev


class Queue:
    def __init__(self, top=None, buffer_size=10):
        self.top = self.last = top
        self.buffer_size = buffer_size

    def put(self, obj):
        if self.empty():
            self.top = self.last = obj
            self.top.prev = self.last
        else:
            self.last.prev = obj
            self.last = obj
        if self.qsize() > self.buffer_size:
            self.top = self.top.prev

    def get(self):
        if not self.empty():
            current_top = self.top
            self.top = self.top.prev
            return current_top.data
        else:
            return 'Queue is empty'

    def empty(self):
        return self.top is None

    def qsize(self):
        if self.empty():
            return 'Queue is empty'

        if self.top == self.last:
            return 1

        counter = 1
        last_obj = self.top
        while last_obj.prev:
            counter += 1
            last_obj = last_obj.prev
        return counter


qu = Queue()
for i in range(1, 101):
    qu.put(QueueObj(i))
print(qu.qsize())
for i in range(11):
    print(qu.get())
