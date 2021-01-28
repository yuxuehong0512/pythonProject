#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author  :xiaoyu
# time    :2021/1/28 21:33
import xlwt#引用的库
import random

data = ['class', 'id', 'swre']#定义函数
file_name = 'yu.xls'


def insert_excel(data, file_name):
    '''
    新建excle表格并插入100行3列数据
    :param data:
    :param file_name: 新文件名
    :return:
    '''
    if not file_name.endswith('.xls'):#如果没有同名的excle新建一个
        file_name += '.xls'#文件最后的格式为.xls
    workbook = xlwt.Workbook(encoding='utf-8')#文件编码为'utf-8'
    ws = workbook.add_sheet("sheet1")#表名为”sheet“

    ws.write(0, 0, label=data[0])#第0行第0列插入data第0个数据
    ws.write(0, 1, label=data[1])#第0行第1列插入data第1个数据
    ws.write(0, 2, label=data[2])#第0行第2列插入data第2个数据

    for j in range(1, 101):
        s = str(random.uniform(0, 1))#将s转化为str类型，random.uniform(0, 1)是将s赋值为0到1中的一个小数
        h = ["Sweet potato", "potatoes", "corn"]#给h赋值为list类型
        b = random.sample(h, 1)#b为h中任意一个值
        ws.write(j, 0, b)#第j行第0列插入b中的一个数据
        ws.write(j, 1, str(j) + ".jpg")#第j行第1列插入数字+.jpg中的一个数据
        ws.write(j, 2, s)#第j行第2列插入s中的一个值
#注意将参数放在for循环下面

    workbook.save(file_name)#保存数据


insert_excel(data, file_name)