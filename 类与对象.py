'''
创建类的语法
class Student:
    pass
包含：
类属性，实例方法，静态方法，类方法
'''


class Student:
    # 类属性
    # 类似c艹类静态属性
    native_place = '南京'

    def __init__(self, place, name):
        self.native_place = place
        # 类实例的属性
        self.name = name
        # 没有专门的修饰符标识私有属性
        # 不希望该属性在类外被访问在属性名前加__
        # 尽管是私有的，但是还是能通过dir()方法获取对应属性名
        # 即_类名__私有属性,通过该名称获取私有属性

    # 实例方法
    def eat(self):
        print('吃饭ing')

    # 两种调用方式：  实例.eat() Student.eat(实例)

    # 静态方法
    # 没有默认参数，使用类名直接访问
    @staticmethod
    def meth1():
        print("static method")

    # 类方法
    # 默认参数cls(class)，使用类名直接访问
    @classmethod
    def classmeth1(cls):
        print("class method")


'''
对象的创建：
实例名 = 类名(参数们)
'''


class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, self.age)


people1 = People('张三', 20)
people1.eat()
'''
动态绑定
希望实例拥新的属性
可以动态绑定属性和方法
'''
people2 = People("李四", 21)
people2.gender = '女'


def show():
    print("类外函数")


people2.show = show
people2.show()
'''
继承：
class 子类类名(父类们):
    pass

没有继承任何类则默认继承Object
支持多继承
定义子类时，必须在其构造函数内调用父类构造函数
'''


class People2(People):

    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def eat():
        print("重写的eat()")


people3 = People2('王五', 25, '男')
'''
方法的重写：
自立中对方法体重新编写
子类重写的方法中可以调用父类被重写的方法super().method()

Object类
所有类的父类
所有类具有object类的属性和方法
可以用dir()查看其属性

object有__str__()方法，用于返回对象的描述
经常被重写


多态：
静态语言 动态语言区别
静态语言实现多态的必要条件：
1.继承
2.方法重写
3.父类引用指向子类对象

动态语言：
不关心对象是什么类型，只关心对象的行为

特殊属性和方法：
特殊属性:
__dict__: 获得类对象或实例对象所绑定的所有属性和方法的字典
__class__: 输出对象所处的类
__bases__: 所有父类类型
__base__: 输出继承()中第一个父类
__mro__: 类的层次结构

特殊方法:
__len__(): 内置len()的参数可以改成自定义类型
__add__(): 使自定义对象具有+功能
__new__(): 创建对象
__init__(): 对创建的对象进行初始化
__subclasses__(): 获取子类列表
'''
'''
类的浅拷贝和深拷贝
变量的赋值操作：
形成两个变量，但指向同一个对象

浅拷贝：
import copy 函数:copy.copy()
对象包含的子(类)对象不拷贝，则生成对象与原对象的子(类)对象指向同一个对象
主对象开辟新空间，子对象地址不变

深拷贝：
import copy 函数:copy.deepcopy()
递归拷贝所有子对象，主对象内所有子对象地址与原对象的子对象的地址均不同
'''
