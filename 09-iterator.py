# 借助 list 的迭代器
class Data(object):
    def __init__(self):
        self._data = []
    def add(self, x):
        self._data.append(x)
    def data(self):
        return iter(self._data)

d = Data()
d.add(1)
d.add(2)
d.add(3)
for x in d.data():
    print(x)
"""
1
2
3
"""

# 标准迭代器
class Data(object):
    def __init__(self, *args):
        self._data = list(args)
        self._index = 0
    
    def __iter__(self):
        return self
    
    # Python 3 写法
    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration()
        d = self._data[self._index]
        self._index += 1
        return d

    # 兼容 Python 2
    def next(self):
        return self.__next__()

d = Data(1, 2, 3)
for x in d:
    print(x)
"""
1
2
3
"""

