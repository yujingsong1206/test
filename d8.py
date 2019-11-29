# import math
# print(math.pi)
#sin(pi/2) 90
# print(math.sin(math.pi/2))
# import random
# num = random.random() * 10 # [0-10) 随机数
# print(num)

import d7 as t1
t1.add2(t1.a,2)
#包
#不能形成闭环

#使用模块的形式定义函数import
#函数:1.求平和 1*1+3*3+4*4
#     2.检测传入的字典（只包含字符串），当value的长度
#       超过2（包含2），就删除超过的长度。
#       比如value='abcd'  删除后value='ab'
#       a = {"key1":"value1","key2":"ab"}
#       删除后 value1--->va     ab ----> ab

#模拟抽奖
#中奖等级：一等奖，二等奖，三等奖
#中奖的范围:
#          [0,0.05)一等奖
#          [0.05,0.4)二等奖
#          [0.4,1.0)三等奖
#模拟这次有1000个人来参加活动，最后输出各个奖项的中奖人数
#判断中的是几等奖 写成一个函数