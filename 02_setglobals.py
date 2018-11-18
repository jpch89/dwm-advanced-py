# 设置全局变量

# 粗暴的写法：通过 exec
data1 = {'a': 1, 'b': 2}
for k, v in data1.items():
    exec('{}={}'.format(k, v))
print('a=%s' % a)
print('b=%s' % b)
"""
a=1
b=2
"""


# 文艺的写法：对 globals() 返回的字典使用 update()
data2 = {'c': 3, 'd': 4}
globals().update(data2)
print('c=%s' % c)
print('d=%s' % d)
"""
c=3
d=4
"""

# 直接对 a 重新赋值
globals()['a'] = '你好'
print('a=%s' % a)
"""
a=你好
"""
