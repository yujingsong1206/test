#可变：  内存地址不变，值可变
#不可变：内存地址不变，值可不变
# d = [1,2,3,'a','d'] #列表
# print(d)
# print(id(d))
# d[0] = 10
# print(d)
# print(id(d))
# d = [1,2,3,[4,5,6]]
# print(d[3][0])
# d = list()
# print(d)
# d = list('abc')
# print(d)

# d = [1,2,3,4]
# print(d[1:3])
# d[1:3] = [10,20,30]
# print(d)
# d[1:4] = []
# print(d)

# print([] and [1,3,4])#false
# print([] or [1,3,4])#true
a = [1,2,4,8,5]
# a.sort(reverse=True)
b = sorted(a, reverse=True)
print(b)
print(a)
