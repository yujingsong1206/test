# a = {1:'1111',2:'2222'}
# a[3] = '3333'
# print(a)
# del a[1]
# print(a)
# a[3] = '4444'
# print(a)
# a = {1:'1111',2:'2222'}
# a = {1,1,1,1,2}
# print(a)
# b = {2,3}
# print(a | b)
# print(type(a))
# a = {}
# print(type(a))
# b = set()
# print(type(b))
# for(int i = 10; i > 0; i--){

# }
# for a in range(0,10):
#     print(a)
# num = 1
# while num <= 20:
#     print(str(num), end=' ')
#     num += 1

# num = 1
# while num <= 20:
#     if(num % 5 == 0):
#         print(num)
#     else:
#         print(num, end=' ')
#     num += 1

# num = 1
# while num < 10:
#     temp = 1
#     while temp <= num:
#         if(temp == num):
#             print('{0}*{1}={2}'.format(temp,num,temp*num))
#         else:
#             print('{0}*{1}={2}'.format(temp,num,temp*num), end=' ')
#         temp += 1
#     num += 1
# sum = 0
# for a in range(1,46):
#     sum += a
# print(sum)
# sum = 0
# num = 1
# while True:
#     if(sum >= 1000):
#         break
#     else:
#         sum += num
#     num += 1
# print(num, sum)

# num = 1
# while num < 10:
#     if(num == 5):
#         num += 1
#         continue
#     print(num)
#     num += 1
# else:
#     print('while结束')

#输入一个年龄，如果年龄输入非法就要求重新输入，直到合法
#最后输出年龄
# age = int(input("请输入年龄"))
# while True:
#     if(age < 0 or age >= 120):
#         age = int(input("年龄不合法，请重新输入："))
#     else:
#         print(age)
#         break

# XXX简单银行系统
# 欢迎来到XXX银行系统
# 1.注册 2.登录 3.查询所有用户 4.修改用户 5.删除用户 6.退出
# 注册：包含卡号（唯一）、姓名、密码、余额
# 登录：卡号和密码来登录
# 	1.查询余额 2.存款 3.取款 4.修改密码 5.退出登录
# 	修改密码成功后，需要退出登录
# 查询所有用户：显示所有用户卡号、姓名、密码、余额
# 修改用户：只能修改用户姓名
# 删除用户
# 保证程序完整
users = {}
print('欢迎来到XXX银行系统')
while True:
    flage = int(input('1.注册 2.登录 3.查询所有用户 4.修改用户 5.删除用户 6.退出  '))
    if flage == 1:
        num = input('请输入卡号：')
        if(num in users):
            print('卡号重复！')
        else:
            name = input('请输入姓名：')
            password = input('请输入密码：')
            users[num] = {'姓名':name,'密码':password,'余额':0.0}
    elif flage == 2:
        pass
    elif flage == 6:
        break
print(users)