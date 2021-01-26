#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author  :xiaoyu
# time    :2021/1/25 14:25
'''
重命名图片、创建文件夹、复制图片
'''

import os
import shutil


def rename_copy(img_root, save_dir):
    '''
    重命名图片、创建文件夹、复制图片
    :param img_root:旧图片储存位置文件夹地址
                文件格式：img_root
                            xxx
                              aaa.jpg
    :param save_dir:新建文件夹储存图片地址
                文件格式:save_dir
                         bbb.jpg
    :return:
    '''
    if not os.path.exists(save_dir): os.mkdir(save_dir)

    # 获取该目录下所有文件，存入列表中
    filelist = os.listdir(img_root)  # 文件夹赋值

    for i in filelist:  # i是filelist下文件夹
        n = 0
        print(i)
        for img in os.listdir(img_root + "/" + i):
            print(img)
            new_img_name = i + str(n + 1) + 'c.JPG'#图片重命名
            file_name = img_root + os.sep + i + os.sep + new_img_name
            os.rename(img_root + i + '/' + img, file_name)
            n += 1
            shutil.copy(file_name, save_dir + new_img_name)

img_root0 = 'D://lianxi/JPGImages/'
save_dir0 = 'D:/lianxi/wenjian/'

rename_copy(img_root=img_root0, save_dir=save_dir0)
