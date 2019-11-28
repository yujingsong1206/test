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
users = {} #{"key1":"value1","key2":"value2"}
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
        #登录：判断卡号是否存在，存在--->判断密码--->登录成功！
        #                      不存在--->提示    --->密码错误--->提示
        num = input('请输入卡号：')
        if(num in users):
            ps = input('请输入密码：')
            if(users[num]['密码'] == ps):
                while True:
                    temp = int(input('1.查询余额 2.存款 3.取款 4.修改密码 5.退出登录  '))
                    if(temp == 1):
                        print("余额：" + str(users[num]['余额']))
                    elif(temp == 2):
                        blance = float(input("请输入存入的余额："))
                        users[num]['余额'] += blance
                    elif (temp == 3):
                        blance = float(input("请输入取出的余额："))
                        if(blance <= users[num]['余额']):
                            users[num]['余额'] -= blance
                        else:
                            print("余额不足")
                    elif (temp == 4):
                        ps = input("请输入修改的密码：")
                        users[num]['密码'] = ps
                        break
                    elif (temp == 5):
                        break
                    else:
                        print("指令输入错误。请重新输入！")
            else:
                print("密码错误")
        else:
            print("卡号不存在")
    elif flage == 3:
        #遍历得到字典的具体值
        #users = {'num':
        #           {'姓名':name,'密码':password,'余额':0.0}}
        if(len(users) == 0):
            print('暂无用户')
        for num in users:
            print("卡号：" + num, end=' ')
            for user in users[num]:
                print(user + ":" + str(users[num][user]), end=' ')
            print()
    elif flage == 4:
        #字典修改值：key值存在就覆盖（修改）
        num = input('请输入卡号：')
        if(num in users):
            name = input('请输入姓名：')
            users[num]['姓名'] = name
        else:
            print("卡号不存在！")
    elif flage == 5:
        #字典的删除：del 字典[key]
        num = input('请输入卡号：')
        if(num in users):
            del users[num]
        else:
            print("卡号不存在！")
    elif flage == 6:
        break
    else:
        print("输入的指令错误，请重新输入！")
print(users)