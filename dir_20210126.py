#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author  :xiaoyu
# time    :2021/1/26 17:26

import os


def dir_rename(file_save):
    '''
    文件夹下多个文件重命名
    :param file_save: 文件夹位置
                文件格式：img_root
    :return:
    '''
    dirs = os.listdir(file_save)  # 文件夹赋值
    i = 100  # 赋值
    num = 0
    for dir1 in dirs:  # for循环逻辑是每次执行for下文件

        s = dir1.split(".")  # s是文件夹格式

        print(s)

        if len(s) > 1:  # 判断s的长度文件夹长度为0

            new_name = file_save + os.sep + str(i) + "." + s[-1]  # 文件重命名

            file_name = file_save + os.sep + dir1  # 旧文件名
            os.rename(file_name, new_name)  # 执行重命名
            print(s)
            i += 2
        else:
            new_name = file_save + os.sep + str(num + 5)
            file_name = file_save + os.sep + dir1
            print(file_name)
            print(new_name)
            os.rename(file_name, new_name)
            num += 3


dir_rename("D:/lianxi/JPGImages")
