#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author  :xiaoyu
# time    :2021/1/27 13:15
def qian(m, n, q):
    '''

    :param m:
    :param n:
    :param q:
    :return:
    '''

    assert q >= 0
    s = 0
    for i in range(0, q + 1):
        # print(i)
        a = m * (1 + n) ** i
        s = a + s
        print("第{}月总金额：".format(i), s)
    return s


qian(1000, 0.005, 360)
