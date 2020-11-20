#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author  :xiaoyu
# time    :2020/11/18 16:07
"""用python设计第一个游戏"""
temp = input("""不妨猜一下小甲鱼现在心里面想的是哪个数字""")
guess = int(temp)
if guess == 8:
    print("你是小甲鱼心里面的蛔虫嘛？！")
    print("猜中了也没有奖励")
else:
     print("猜错了，小甲鱼现在心里面想的是8")
print("游戏结束了，不玩了")