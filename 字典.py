# 无序序列 可变键值对
'''
字典特点：
键值对形式，键不能重复，值可以重复
元素无序，键不可变
字典可以动态伸缩
比较占内存，用空间换时间
'''

# 创建
dict1 = {"gzd": 1, "zxl": 2}
dict2 = dict(gzd='1', zxl=2)

# print(dict1)
# print(dict2)

# 元素的获取
# [] / get()
# print(dict1.get("zxl"))
# print(dict1["gzd"])
# []没有匹配对象会报错
# get()不会报错，返回None

# print(dict1.get("xsb", 10))
# 可以提供不存在时的默认值

# key的判断 in / not in

# 删除
# del删除指定键值对
del dict1["zxl"]
# print(dict1)
# clear() 清空字典元素
# 新增/修改 dict[key] = value

# 获取字典视图操作
# keys() 所有key
# values() 所有value
# items() 所有key-value对
# print(dict2.values(), type(dict2.values()))
# print(list(dict2.values()))

# 字典的遍历
# for item in dict:

# 字典生成式
items = ["apple", "banana", "pitch"]
prices = [10, 20, 30]

dict3 = {items: prices for items, prices in zip(items, prices)}
print(dict3)
dict3 = {items.upper(): prices for items, prices in zip(items, prices)}
print(dict3)
# 当其中一个列表元素多出来的时候，zip()取元素数量更少的
items.append("kiwifruit")
dict3 = {items.upper(): prices for items, prices in zip(items, prices)}
print(dict3)
