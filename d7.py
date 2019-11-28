#函数   round() #四舍五入
#1.功能性
#2.隐蔽性  1）源码 2）bug
#3.避免重复代码的编写

#1.必须参数
def add2(a,b):
    print(a+b)
add2(1,3)

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
def print_student_info(name,age,gender,collge):
    print("姓名：" + name)
    print("年龄" + str(age))
    print("性别：" + gender)
    print("学校：" + collge + "读书")

print_student_info("李淳明",20,"男","昆明理工大学")
print("---------------")
print_student_info(age=20,name="李淳明",gender="男",collge="云大")
 #IndentationError: unindent does not match any outer indentation level
