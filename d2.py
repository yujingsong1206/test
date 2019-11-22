#交换2个变量有哪些方法？
# 1 定义一个中间变量来进行交换
# temp = a
# a = b 
# b = temp
# 2 python独有语法
# a , b = b , a
# print(a)
# print(b)
# 3 加法运算
a = 10
b = 20
# a = a + b
# b = a - b
# a = a - b
# 4 异或运算(相等为0，不等为1)
a = a ^ b # 30
b = a ^ b # 10
a = a ^ b # 20
print(a)
print(b)
print(int(0b11110))
# 0 1 0 1 0
# 1 0 1 0 0
# 1 1 1 1 0
# 0 1 0 1 0
# 1 0 1 0 0
# 面向对象编程？
# 面向监狱编程？