from timeit import timeit
# timeit('语句'[, number=100000])
# timeit('函数名', 'from __main__ import 函数名'[, number=100000])
# timeit('函数名', globals=globals())

from random import randint
# randint(a, b) 生成 [a, b] 的随机数

old_li = [1, 2, 2, 3, 3, 3]
# 列表去重1：list({}.fromkeys(原列表).keys)
# 我叫做：字典取键法
# 如果是 Python 2 的话，最外层不需要用 list 转换
new_li = list({}.fromkeys(old_li).keys())
print(new_li)
"""
[1, 2, 3]
"""

# 列表去重2：list(set(原列表))
# 我叫做：集合法
new_li = list(set(old_li))
print(new_li)
"""
[1, 2, 3]
"""

# 性能分析1：原列表较短的情况
# 字典取键法
# t = timeit('list({}.fromkeys(old_li).keys())', 'from __main__ import old_li')
t = timeit('list({}.fromkeys(old_li).keys())', globals=globals())
print(t)
"""
0.7955012980800552
"""
# 集合法
t = timeit('list(set(old_li))', globals=globals())
print(t)
"""
0.4911843005941092
"""

# 性能分析2：原列表较大的情况
big_li = [randint(1, 50) for i in range(10000)]
# 字典取键法
t = timeit('list({}.fromkeys(big_li).keys())',
    number=10000, globals=globals())
print(t)
"""
2.6739583454187015
"""
# 集合法
t = timeit('list(set(big_li))',
    number=10000, globals=globals())
print(t)
"""
1.1371806004635423
"""
