from d12 import Human
class Studen(Human):
    count = 0#学生人数
    def __init__(self,name,age):
        # Human.__init__(self,name,age)
        super().__init__(name,age)
        self.__score = 0
        self.__class__.count += 1
    def do_homework(self):
        super().do_homework()
        print("做作业")