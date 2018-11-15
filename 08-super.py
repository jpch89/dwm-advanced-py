class LogginDict(dict):
    def __setitem__(self, key, value):
        print('设置{0}为{1}。'.format(key, value))
        dict.__setitem__(key, value)

# 假如后续要修改需要继承的类
# 那么要在类定义处修改一遍，还要在重写的方法里面修改一遍
# 容易忘记

# 更好的做法：
class LogginDict(dict):
    def __setitem__(self, key, value):
        print('设置{0}为{1}。'.format(key, value))
        super(LogginDict, self).__setitem__(key, value)
        # Python 3 写法
        # super().__setitem__(key, value)
