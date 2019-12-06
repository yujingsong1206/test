#模拟抽奖
#中奖等级：一等奖，二等奖，三等奖
#中奖的范围:
#          [0,0.05)一等奖
#          [0.05,0.4)二等奖
#          [0.4,1.0)三等奖
#模拟这次有1000个人来参加活动，最后输出各个奖项的中奖人数
#判断中的是几等奖 写成一个函数
import random
def lucky():
    num = random.random()#[0,1)
    if(0<=num<0.05):
        return "一等奖"
    elif(0.05<=num<0.4):
        return "二等奖"
    else:
        return "三等奖"

def lucky2():
    num = random.random()#[0,1)
    if(0<=num<0.05):
        return "一等奖"
    elif(0.05<=num<0.4):
        return "二等奖"
    else:
        return "三等奖"

def lucky3():
    num = random.random()#[0,1)
    if(0<=num<0.05):
        return "一等奖"
    elif(0.05<=num<0.4):
        return "二等奖"
    else:
        return "三等奖"

# result = {}
# for i in range(0,1000):
#     temp = lucky()
#     if(temp in result):
#         result[temp] += 1
#     else:
#         result[temp] = 1
# print(result)