# vars() 不传递参数就跟 locals() 是一样的
# 它返回当前所有局部变量的字典
print(vars() is locals())
"""
True
"""

import sys
# vars(obj) 相当于 obj.__dict__
print(vars(sys) is sys.__dict__)
"""
True
"""
