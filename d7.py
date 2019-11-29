#函数   round() #四舍五入
#1.功能性
#2.隐蔽性  1）源码 2）bug
#3.避免重复代码的编写

#1.必须参数
a = 1
def add2(a,b):
    print(a+b)
# add2(1,3)

#递归
# maximum recursion depth exceeded
# java python --> 垃圾回收机制（DC）
# c  申请空间  使用完   回收
# 内存泄漏：我使用一片内存空间(10M)，但是以后都不会再使用，可是又不会回收 100M - 10M = 90M
# 内存溢出：系统自动分配内存空间不满足我需要的

# def demo():
#     a = 2
#     if True:
#         b = 1
#     print(b)
# demo()

#2.关键字参数
# def print_student_info(name,age,gender,collge):
#     print("姓名：" + name)
#     print("年龄" + str(age))
#     print("性别：" + gender)
#     print("学校：" + collge + "读书")

# print_student_info("李淳明",20,"男","昆明理工大学")
# print("---------------")
# print_student_info("男",name=20,age="李淳明",collge="云大")
# print_student_info(age=20,name="李淳明",gender="男",collge="云大")
 #IndentationError: unindent does not match any outer indentation level

#3 默认参数
def print_student_info(name,age=18,gender="男",collge="昆明理工大学"):
    print("姓名：" + name)
    print("年龄" + str(age))
    print("性别：" + gender)
    print("学校：" + collge + "读书")

# print_student_info("李淳明")
# print_student_info("杨光明")
# print_student_info(name="虎静",gender="女")

#返回值
def damage(skill1,skill2):
    damage1 = skill1 * 10
    damage2 = skill2 * 2 + 5
    return damage1,damage2
skill1damage,skill2damage = damage(1,2)
#序列解包
# print(skill1damage,skill2damage)

# a,b,c = 1,2,3
# d = 1,2,3
# print(d, type(d))
# a,b,c = d
# print(a,b,c)

#4.不定参数
def print_info(*str):
    print(str)
    print("不定参数：")
    for a in str:
        print(a)
# print_info("a")
# print_info("a","b","c")
# b = (1,2,3)
# print_info(*b)

def print_info1(**str):
    # print(str)
    for k,v in str.items():
        print(k,v)
# print_info1(**{"1":10,"2":20})
