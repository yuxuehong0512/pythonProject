#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author  :xiaoyu
# time    :2021/1/26 17:26

import os

"""多个文件夹重命名"""
def dir_rename(file_save,new_name_file):
    '''
    :param dir: 旧文件夹位置
                文件格式：img_root
                              aaa.xxx
    :param new_name_file: 新文件夹位置
                        文件格式：img_root
                              aaa.xxx
    :return: 
    '''

    file_save = 'D:/lianxi/JPGImages/'#文件夹路径

    dirs = os.listdir(file_save)  # 文件夹赋值
    i=1#赋值
    num = 0
    for dir1 in dirs:  # for循环逻辑是每次执行for下文件

        s = dir1.split(".")#s是文件夹格式

        print(s)

        if len(s) > 1:#判断s的长度文件夹长度为0

            new_name_file = file_save + str(i) + "." + s[-1]#文件重命名

            file_name = file_save + dir1#旧文件名
            os.rename(file_name, new_name_file)#执行重命名
            print(s)
            i += 2
        else:
            new_name_file = file_save + str(num + 1)
            file_name = file_save + dir1
            print(file_name)
            os.rename(file_name, new_name_file)
            num += 3
