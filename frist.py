#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author  :xiaoyu
# time    :2020/11/18 16:07

"""用python设计第一个游戏"""
temp = input("""不妨猜一下小甲鱼现在心里面想的是哪个数字""")
guess = int(temp)
while guess != 8:
    temp = input("""小老妹，猜错了，继续猜吧""")
    guess = int(temp)
    if guess == 8:
        print("你是小鱼心里面的蛔虫嘛？！")
        print("猜中了也没有奖励")
    else:
          if guess >= 8:
              print("小老妹，大了，大了")
          else:
              print("小老妹，小了小了")
print("游戏结束了，不玩了")
# teatch = '小鱼'
# print(teatch)
# first = 3
# second = 2
# third = first + second
# print(third)
# myteatch = 'xiaojiayu'
# yourteatch = 'heiye'
# ourteatch = myteatch + yourteatch
# print(ourteatc)
# str = 'C:\now'
# print(str)
# str = 'C:\now\wast\w1wfer\drfvr'
# print(str)
# str = r'C:\now\wast\w1wfer\drfvr'
# print(str)
# input(teatch)
# if teatch > 4:
#     print()

