# 省略字段名传递位置参数
print('我叫{}，今年{}岁。'.format('小明', 18))
"""
我叫小明，今年18岁。
"""

# 花括号个数可以少于位置参数的个数
print('我爱吃{}和{}。'.format('香蕉', '苹果', '大鸭梨'))
"""
我爱吃香蕉和苹果。
"""

# 花括号个数多于位置参数的个数则会报错
# print('我还吃{}和{}。'.format('西红柿'))
"""
IndexError: tuple index out of range
"""


# 通过数字形式的简单字段名传递位置参数
print('身高{0}，家住{1}。'.format(1.8, '铜锣湾'))
"""
身高1.8，家住铜锣湾
"""

# 数字形式的简单字段名可以重复使用。
print('我爱{0}。\n她今年{1}。\n{0}也爱我。'.format('阿香', 17))
"""
我爱阿香。
她今年17。
阿香也爱我。
"""

# 体会把所有位置参数整体当成元组来取值
print('阿香爱吃{1}、{3}和{0}。'.format(
    '榴莲', '臭豆腐', '皮蛋', '鲱鱼罐头', '螺狮粉'))
"""
阿香爱吃臭豆腐、鲱鱼罐头和榴莲。
"""

# 尝试一下越界错误
# print('{1}'.format('错误用法'))
"""
IndexError: tuple index out of range
"""

# 使用变量名形式的简单字段名传递关键字参数
print('我大哥是{name}，今年{age}岁。'.format(name='阿飞', age=20))
"""
我大哥是阿飞，今年20岁。
"""

# 关键字参数的顺序可以随意调换
print('我大哥是{name}，今年{age}岁。'.format(age=20, name='阿飞'))
"""
我大哥是阿飞，今年20岁。
"""

# 混合使用数字形式和变量名形式的字段名
# 可以同时传递位置参数和关键字参数
print('这是一个关于{0}、{1}和{girl}的故事。'.format(
    '小明', '阿飞', girl='阿香'))
"""
这是一个关于小明、阿飞和阿香的故事。
"""

# 但是关键字参数必须位于位置参数之后
# print('这是一个关于{0}、{1}和{girl}的故事。'.format(
    # '小明', girl='阿香' , '阿飞'))
"""
SyntaxError: positional argument follows keyword argument
"""

# 数字也可以省略
print('这是一个关于{}、{}和{girl}的故事。'.format(
    '小明', '阿飞', girl='阿香'))

# 但是省略字段名不能和数字形式的字段名同时出现
# print('这是一个关于{}、{1}和{girl}的故事。'.format(
#     '小明', '阿飞', girl='阿香'))
"""
ValueError: cannot switch from automatic field numbering to manual field specification
"""

# 使用元组传参
infos = '钢铁侠', 66, '小辣椒'
print('我是{}，身价{}亿。'.format(*infos))
"""
我是钢铁侠，身家66亿。
"""
print('我是{2}，身价{1}亿。'.format(*infos))
"""
我是小辣椒，身家66亿。
"""

# 使用字典传参
venom = {'name': '毒液', 'weakness': '火'}
print('我是{name}，我怕{weakness}。'.format(**venom))
"""
我是毒液，我怕火。
"""

# 同时使用元组和字典传参
hulk = '绿巨人', '拳头'
captain = {'name': '美国队长', 'weapon': '盾'}
print('我是{}, 我怕{weapon}。'.format(*hulk, **captain))
print('我是{name}, 我怕{1}。'.format(*hulk, **captain))

"""
我是绿巨人, 我怕盾。
我是美国队长, 我怕拳头。
"""

# 同时使用位置参数、元组、关键字参数、字典传参
# 注意：
# 位置参数要在关键字参数前面
# *元组要在**字典前面
tup = '鹰眼',
dic = {'weapon': '箭'}
text = '我是{1}，我怕{weakness}。我是{0}，我用{weapon}。'
text = text.format(
    *tup, '黑寡妇', weakness='男人', **dic)
print(text)
"""
我是黑寡妇，我怕男人。我是鹰眼，我用箭。
"""


# 复合字段名中使用点号传递对象属性
class Person:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr


p = Person('辣妹子', '重庆')

# 点号用法：传递位置参数
print('我是{0.name}，家在{0.addr}。'.format(p))
"""
我是辣妹子，家在重庆。
"""

# 当只有一个替换字段的时候可以省略数字
print('{.name}辣！'.format(p))
"""
辣妹子辣！
"""

# 试试传递文件对象的属性
f = open('out.txt', 'w')
print('文件名为：{.name}'.format(f))
f.close()
"""
文件名为：out.txt
"""

# 点号用法：传递关键字参数
print('我是{girl.name}，家在{girl.addr}。'.format(girl=p))
# 和上一句等价
print('我是{p.name}，家在{p.addr}。'.format(p=p))
"""
我是辣妹子，家在重庆。
我是辣妹子，家在重庆。
"""

# 方括号用法：用列表传递位置参数
infos = ['阿星', 9527]
food = ['霸王花', '爆米花']
print('我叫{0[0]}，警号{0[1]}，爱吃{1[0]}。'.format(
    infos, food))
"""
我叫阿星，警号9527，爱吃霸王花。
"""

# 方括号用法：用元组传递位置参数
food = ('僵尸', '脑子')
print('我叫{0[0]}，年龄{1}，爱吃{0[1]}。'.format(
    food, 66))
"""
我叫僵尸，年龄66，爱吃脑子。
"""

# 方括号用法：用字典传递位置参数
dic = dict(name='阿星', pid=9527)
print('我是{[name]}！'.format(
    dic))
# 多个替换字段，不能省略数字
print('我是{0[name]}，警号{0[pid]}。'.format(
    dic))
"""
我是阿星！
我是阿星，警号9527。
"""

# 方括号用法：传递关键字参数
names = ['皮卡丘']
dic = {'name': '妙蛙花'}
skills = ('十万伏特', '飞叶快刀')
text = '我是{names[0]}，我会{skills[0]}。我是{dic[name]}，我会{skills[1]}。'
text = text.format(names=names, skills=skills, dic=dic)
print(text)
"""
我是皮卡丘，我会十万伏特。我是妙蛙花，我会飞叶快刀。
"""

# 转换字段
print('I am {!s}!'.format('Bruce Lee 李小龙'))
print('I am {!r}!'.format('Bruce Lee 李小龙'))
print('I am {!a}!'.format('Bruce Lee 李小龙'))
"""
I am Bruce Lee 李小龙!
I am 'Bruce Lee 李小龙'!
I am 'Bruce Lee \u674e\u5c0f\u9f99'!
"""

# 格式说明符本身可以是字段名
print('{0:{1}}'.format(3.14159, '.4f'))
"""
3.1416
"""

# 正负号
print('{:哈=+8.2f}'.format(3.14159))
print('{:哈=+8.2f}'.format(-3.14159))
print('{:哈=+8.2f}'.format(0))
print('{:哈=+8.2f}'.format(-0))
"""
+哈哈哈3.14
-哈哈哈3.14
+哈哈哈0.00
+哈哈哈0.00
"""

# 对于非数字类型，精度指定最大字段宽度
print('{0:.3}'.format('哇哈哈哈哈哈'))
"""
哇哈哈
"""

# 整数类型不能指定精度
# print('{:.3d}'.format(666))
"""
ValueError: Precision not allowed in integer format specifier
"""

# 分组选项 ,
print('数字：{0:,.2f}'.format(6666.6666))
"""
数字：6,666.67
"""

# n 类型使用本地化的分组选项 ,
# 此项报错，我怀疑是因为中文没有数字的分隔符
# print('数字：{0:,n}'.format(6666))
"""
ValueError: Cannot specify ',' with 'n'.
"""
# 使用 d 类型确实是可以的
print('数字：{0:,d}'.format(6666))
"""
数字：6,666
"""

# 分组选项 _ 作用于浮点数
print('数字：{0:_.2f}'.format(6666.6666))
"""
数字：6_666.67
"""

# 分组选项 _ 作用于 d 类型
print('数字：{0:_d}'.format(6666))
"""
数字：6_666
"""

# 分组选项 _ 作用于 b 类型
print('数字：{0:_b}'.format(0b100111011))
"""
数字：1_0011_1011
"""
# 分组选项 _ 作用于 o 类型
print('数字：{0:_o}'.format(0o426754316))
"""
数字：4_2675_4316
"""
# 分组选项 _ 作用于 x 类型
print('数字：{0:_x}'.format(0x2a846e98d))
"""
数字：2_a846_e98d
"""
# 分组选项 _ 作用于 X 类型
print('数字：{0:_X}'.format(0X2a846e98d))
"""
数字：2_A846_E98D
"""
# 分组选项 _ 作用于其他类型（比如 n 类型）
# print('字符串：{0:_n}'.format(1234567))
"""
ValueError: Cannot specify ',' with 'n'.
"""

# s 类型
print('{0:s}'.format('略略略'))
# s 类型可以省略
print('{0:}'.format('略略略'))
"""
略略略
略略略
"""

# b 类型：二进制
print('{0:b}'.format(3))
"""
11
"""

# c 类型：把整数转换成 unicode 字符
print('{:c}'.format(97))
"""
a
"""

# d 类型：十进制整数
print('{:d}'.format(666))
"""
666
"""

# o 类型：八进制数
print('{:o}'.format(10))
"""
12
"""

# x 类型：十六进制数，a到f小写
print('{:x}'.format(15))
"""
f
"""

# X 类型：十六进制数，A到F大写
print('{:X}'.format(15))
"""
F
"""

# n 类型：与d相同，会插入本地化的分隔符
print('{:n}'.format(66666))
# 经试验，本机无法为 n 指定任何分组选项（,_）
# print('{:,n}'.format(66666))
"""
ValueError: Cannot specify ',' with 'n'.
"""
# print('{:_n}'.format(66666))
"""
ValueError: Cannot specify ',' with 'n'.
"""

# e 类型：科学记数法
# 默认精度为 6 位
print('{:e}'.format(1234567.1234567))
"""
1.234567e+06
"""

# E 类型：与 e 相同，用大写 E 表示指数
# 默认精度为 6 位
print('{:E}'.format(1234567.1234567))
# 修改精度为 10 位
print('{:.10E}'.format(1234567.1234567))
"""
1.234567E+06
1.2345671235E+06
"""

# f 类型
# 默认精度为 6 位
print('{:f}'.format(1234567.1234567))
"""
1234567.123457
"""

# F 类型
nan = float('nan')
inf = float('inf')
print('{:F}\n{:F}'.format(nan, inf))
"""
NAN
INF
"""


# 打印花括号需要使用花括号转义
print('{{{}}}'.format('张无忌'))
"""
{张无忌}
"""

# g 类型
print('{:g}'.format(1234567.1234567))
print('{:g}'.format(1234.1234))
"""
1.23457e+06
1234.12
"""

# G 类型
print('{:G}'.format(1234567.1234567))
print('{:G}'.format(1234.1234))
"""
1.23457E+06
1234.12
"""

# n 类型
print('{:n}'.format(1234567.1234567))
print('{:n}'.format(1234.1234))
"""
1.23457E+06
1234.12
"""

# 经试验，本机指定分组选项会报错
# print('{:,n}'.format(1234.1234))
"""
ValueError: Cannot specify ',' with 'n'.
"""
# print('{:_n}'.format(1234.1234))
"""
ValueError: Cannot specify ',' with 'n'.
"""

# % 类型
print('{:%}'.format(1))
"""
100.000000%
"""
