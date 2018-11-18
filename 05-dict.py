# 使用可迭代对象构造字典
d = dict((['a', 1], ['b', 2]))
print(d)
"""
{'a': 1, 'b': 2}
"""

# zip 对象也是可迭代的，所以可以用来构造字典
d = dict(zip('ab', range(2)))
print(d)
"""
{'a': 0, 'b': 1}
"""

# map 对象同样也是可迭代的
m = map(lambda x: (x, x ** 2), [2, 3])
from collections import Iterable
print(isinstance(m, Iterable))
"""
True
"""
d = dict(m)
print(d)
"""
{2: 4, 3: 9}
"""

# 注意，map 对象使用过一次之后就没有值了
# 因为已经迭代完毕
m = map(lambda x: x, range(5))
print(list(m))
print(list(m))
"""
[0, 1, 2, 3, 4]
[]
"""

# dict.fromkeys 方法生成字典
# 需要传递一个可迭代对象
d = dict.fromkeys('abc')
print(d)
"""
{'a': None, 'b': None, 'c': None}
"""

# 还可以提供默认值
d = {}.fromkeys(range(3), '呵呵')
print(d)
"""
{0: '呵呵', 1: '呵呵', 2: '呵呵'}
"""

# 如果提供列表作为默认值
# 则字典所有的值都指向一个列表
d = {}.fromkeys('ab', [1])
print(d)
d['a'].append('变')
print(d)
"""
{'a': [1], 'b': [1]}
{'a': [1, '变'], 'b': [1, '变']}
"""

# 字典解析生成字典
d = {k: v for k, v in zip('abc', range(3))}
print(d)
"""
{'a': 0, 'b': 1, 'c': 2}
"""

# 花括号语法生成字典
d = {'name': '狗子', 'age': 2}
print(d)
"""
{'name': '狗子', 'age': 2}
"""

# setdefault(键, 默认值) 的用法
d = {'苹果': 6, '香蕉': 8}
ret = d.setdefault('苹果', 0)
print(f'苹果有{ret}个！')
ret = d.setdefault('火龙果', 0)
print(f'火龙果有{ret}个！')
"""
苹果有6个！
火龙果有0个！
"""
