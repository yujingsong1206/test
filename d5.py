# d = {}
# print(type(d))
# d = {'Q':'元素之怒','W':'方圆','E':'天之勇','R':'大'}
# d['被动'] = '凌气'
# print(d)
# print(d)
# for e in d:
#     print(d[e],end=' ')
# for e in d.values():
#     print(e)
# e = {'1':'1','2':'2'}
# d = dict(e)
# print(id(e),id(d))

#定义一个LOL英雄名字字典(把字典类似的当成一个假(类))
#1.控制台输入选择英雄
#2.打印输出我选择的英雄是谁，并且包含哪些技能
#（我选择的英雄是：张三，所属技能：嘴炮 女装）
#3.保证程序逻辑完整性
# heros = {'瑞兹':{'Q':'超负荷','W':'符文禁锢','E':'法术涌动','R':'大曲境折跃'},'奇亚娜':{'Q':'元素之怒','W':'方圆塑令','E':'天纵之勇','R':'惊才绝景'}}
# print('可选择的英雄：')
# for name in heros:
#     print(name, end=' ')
# print()
# name = input('请选择英雄：')
# if(name in heros):
#     print('我选择的英雄：' + name)
#     print('所属的技能：', end='')
#     for skill in heros[name]:
#         print(heros[name][skill], end=' ')
# else:
#     print('没有你选择的英雄')

heros = {1:{'瑞兹':{'Q':'超负荷','W':'符文禁锢','E':'法术涌动','R':'大曲境折跃'}},2:{'奇亚娜':{'Q':'元素之怒','W':'方圆塑令','E':'天纵之勇','R':'惊才绝景'}}}
print('可选择的英雄：')
for index in heros:
    print(index, end='.')
    for name in heros[index]:
        print(name, end=' ')
index = int(input('请选择英雄（序号）：'))
if(index in heros):
    for name in heros[index]:
        print('我选择的英雄是：' + name)
        print('所属的技能：',end='')
        for skill in heros[index][name]:
            print(heros[index][name][skill],end=' ')
else:
    print('没有你要选择的英雄')