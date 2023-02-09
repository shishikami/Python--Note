# 一个变量存储更多信息
# 创建方式 [] 或者list()

list1 = ["zxl", "gzdsb"]
list2 = list(["zxl", "gzdsb"])
print(list1)
print(list2)

# 按顺序有序排列，索引映射唯一数据
# 可存储重复数据，任意数据类型共存
# 根据需要动态分配、回收内存

# index()
# 返回第一个匹配的值，若不存在则抛出异常
# 可以指定start stop
num1 = list1.index("zxl")
print(num1)

# 索引位置
#  0  1  2  3
# -4 -3 -2 -1
'''
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list3[::])
print(list3[:9:])
print(list3[-1::-1])
print(list3[:-9:-1])
print(list3[6::-1])
'''

# 切片为列表的部分拷贝

# 判断元素在列表中是否存在
# in / not in

# 增删改操作
# append() 列表末尾添加一个元素
# extend() 末尾添加至少一个元素
# insert() 在任意位置添加一个元素
# 切片 在任意位置添加一个元素
'''
list4 = []
list4.append(1)
print(list4)
list5 = [2, 3]
# 将列表当作元素添加
list4.append(list5)
# 在末尾添加多个元素
list4.extend(list5)
print(list4)

list4.insert(0, 10)
print(list4)

list6 = ['a', 'b', 'c']
# 切除部分被新列表替换
list6[1:] = list4
print(list6)
'''

# remove() 删除指定元素，如果有多个只删除第一个，没有则报错
# pop() 删除指定索引上的元素，索引不存在报错，不写索引默认最后一个元素
# 切片
# clear 清空列表
# delete 删除列表

# 索引值修改
# 切片法修改

# 排序
list7 = [1, 4, 345, 23, 85, 23, 88, 0]

# sort() 不生成新对象 可选 reverse = True/False
list7.sort()
print(list7)
list7.sort(reverse=True)
print(list7)

# sorted() 产生新列表对象
list7_new = [1, 76, 23, 623, 2, 0, 342]
list8 = sorted(list7_new)
print(list8)

# 列表生成式
list9 = [i for i in range(1, 10)]
print(list9)
