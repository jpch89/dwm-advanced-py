d1 = dict(a=1, b=2)
d2 = dict(b=2, c=3)
print(d1)
print(d2)
"""
{'a': 1, 'b': 2}
{'b': 2, 'c': 3}
"""

# 尝试取交集，失败！
# print(d1 & d2)
"""
TypeError: unsupported operand type(s) for &: 'dict' and 'dict'
"""

# 但是使用 items 可以
# 注意：Python 2 中是 viewitems
i1 = d1.items()
i2 = d2.items()

# 交集
print(i1 & i2)
# 得到一个集合
print(type(i1 & i2))
"""
{('b', 2)}
<class 'set'>
"""
# 需要手动转换成字典
res = dict(i1 & i2)
print(res)

# 并集
print(dict(i1 | i2))
"""
{'c': 3, 'a': 1, 'b': 2}
"""

# 差集（仅 i1 有，i2 没有的）
print(dict(i1 - i2))
"""
{'a': 1}
"""

# 对称差集（不同时出现于 i1 和 i2 中）
print(dict(i1 ^ i2))
"""
{'c': 3, 'a': 1}
"""
