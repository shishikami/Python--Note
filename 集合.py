# 可变序列 无序
# 没有value的字典

# 创建
s1 = {1, 22, 3, 4, 5, 6, 6}
s2 = set({1, 2, 3, 4})
s3 = set([1, 2, 4, 9, 16, 25])
s4 = set("Python")
s5 = set((1, 9, 20, 35))
# print(s)
print(s4)
print(s5)

# 定义空集合
# 直接写{}将会是dict
s6 = set()

# 判断操作
# in / not in

# 新增
# add() 一次添加一个元素
# update() 一次添加至少一个元素 可以添加列表/元组，会转化为集合再添加

# 删除
# remove() 删除指定元素，不存在抛出Error
# discard() 删除指定元素，不存在不会抛出异常
# pop() 一次删除任意一个元素 无参数，不能指定参数
# clear() 清空集合

# 集合间关系
# 两个集合是否相等 == !=
# 是否是另一个集合的子集 issubset()
# 是否是另一个集合的超集 issuperset()
# 是否没有交集 isdisjoint()

# 数学操作
# 交集 intersection() 或 &
s7 = {1, 2, 3, 4, 5}
s8 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s7.intersection(s8))
print(s7 & s8)
# 并集 union() 或 |
print(s7 | s8)
# 差集 difference() 或 -
print(s7.difference(s8))
# 对称差 symmetric_difference() 或 ^
print(s7.symmetric_difference(s8))

# 集合生成式
s9 = {i for i in range(10)}
print(s9)
