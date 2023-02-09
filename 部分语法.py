# range()
# range(stop) [0,stop)
# range(start, stop) [start, stop)
# range(start, stop, step) [start, stop)步长为step
# 返回值是迭代器对象，占用内存是固定的，仅当使用的时候才会计算实际内存需求

r = range(10)
print(r)
print(list(r))

# for in 循环
# 从字符串、序列中依次提取值，对象必须可以遍历
# 不需要使用提取的变量可以用_占位
for item in "Python":
    print(item)
