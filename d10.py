#类是现实世界或现实世界中的实体在计算机中的反映
#它把数据和数据的操作都封装在一起
#类首字母大写，驼峰命名
#函数、变量小写 student_info()
#类 面向对象  怎么才能设计好一个类  设计模式
#类 对象
class Student():
    #类体
    count = 0#学生人数
    #构造函数 #默认返回值None，同时只能是None
    #类变量:所有的实例可以共享 实例变量:一个实例独有
    #成员变量：可见性  public  private
    def __init__(self,name,age):#self不是关键字 实例方法
        self.name = name
        self.age = age
        self.__score = 0
        # Student.count += 1
        # self.__class__.count += 1
    def do_homework(self):
        print("做作业")
    def set_score(self,score):
        self.__score = score
    # def __del__(self):
    #     print("student销毁")
    @classmethod
    def puls_count(cls):#类方法
        cls.count += 1
    
    # @staticmethod
    # def add(x,y):
    #     return x+y
    
# class PrintInfo():
#     def print_info(self):
#         print("姓名:" + self.name)
#         print("年龄" + str(self.age))

# student1 = Student("石敢当",18)
# student2 = Student("刘大壮",20)
# student1.set_score(90)
# print(Student.__dict__)
# print(student2.__dict__)
# print(student1.name,student2.name)#石敢当 刘大壮
# print(student1.count,Student.count)#2 2

#类 对象
#类变量 实例变量
#类方法  实例方法  静态方法
#成员可见性 publi private
#继承