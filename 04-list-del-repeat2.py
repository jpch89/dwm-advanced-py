l = [1, 2, 4, 7, 2, 1, 8, 6, 1]
# 字典取键法可以保证原列表元素顺序
print(list(dict.fromkeys(l).keys()))
# 集合法则不可以
print(list(set(l)))

# 还有一种方法：有序字典取键法
# 其实在 Python 3.6 及后续版本这个方法等价于字典取键法
from collections import OrderedDict
print(list(OrderedDict.fromkeys(l).keys()))
