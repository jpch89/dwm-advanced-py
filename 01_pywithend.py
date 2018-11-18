# Python 可以有 end
__builtins__.end = None


def pos_or_neg(x):
    if x > 0:
        print(str(x) + '是正数')
    else:
        print(str(x) + '是负数')
    end
end


def main():
    pos_or_neg(1)
    print('Python 可以使用 end！')
end


main()
"""
1是正数
Python 可以使用 end！
"""
