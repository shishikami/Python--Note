'''
模块 Modules
一个模块可以包含诸多函数
一个.py的文件就是模块
可以包含函数、类、语句

方便程序和脚本的导入
避免函数名和变量名冲突
提高维护性和重用性

写法：
import 模块名称 as 别名
from 模块名称 import 函数/类/变量

以主程序形式进行：
模块包含具有模块名称的属性__name__
顶级模块名称为__main__

if __name__ == '__main__':
    只有该模块为顶级模块时才执行

python包:
功能相近的模块组合在一起
代码规范，避免模块名冲突

包含__init__.py的文件的目录为包

import 包名.模块名
'''
'''
常用内置模块：
sys: 与python解释器和环境相关操作的标准库
time: 提供与事件相关的各种函数的标准库
os: 访问操作系统服务功能
calendar: 与日期相关的各种函数
urllib: 读取来自网上的数据
json: 使用json序列化和反序列化对象
re: 字符串中执行正则表达式
math: 标准算术运算
decimal: 控制运算精度有效位数四舍五入的十进制操作
logging: 事件记录...
'''
