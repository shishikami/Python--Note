# Bug分类
'''
1. Syntax Error
input返回str 不做转化就用
中英文标点
变量未定义等等

2. IndexError
索引越界

3.KeyError
映射中没有这个键

4.NameError
未声明/初始化对象，没有属性

5.ValueError
传入无效参数
'''
'''
try:
    ...
except ...Error:
    ...
可以多个except
else:
finally:
无论是否产生异常都会执行
'''
try:
    divide = int(input())
    10 / divide
except BaseException as e:
    print(e)
else:
    print('正确的')
finally:
    print("Finally")
'''
异常处理模块
import traceback

except:
    traceback.print_exc()
'''
