#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author  :xiaoyu
# time    :2021/1/24 14:24
#x = 3
#y = 5
#x,y = y,x
#print(x,y)
#print("let's go")
#print('let\'s go')
#print("a\nb\nc\nd")
#print("a\b\c\d")
#print(1 + 1)
#print("1" + "1")
#print("每天爱你3000遍\n" * 3000)
#abcd = input("你是谁:")
#"你是谁: = 我是你爸爸"
#print(abcd)
#wasd = input("请输入一个数字")
#guess = int(wasd)
#print(guess)
"""用python设计一个游戏"""
import random
huaner = 5
answei = random.randint(1,10)
while huaner > 0:
    youxi = input("不妨猜猜小鱼心里想的啥")
    guess = int(youxi)
    if guess == answei:
        print("你是我肚子里的蛔虫嘛")
        print("奖励200个mua\n" * 200)
        break
    else:
        if guess < 8:
            print("小笨蛋小了")
        else:
            print("大了大了")
        huaner = huaner -1
print("游戏结束")

import zuoye1

zuoye1.rename_capy()