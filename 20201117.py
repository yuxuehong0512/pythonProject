# zuozhe  :xiaoyu
# time    :2020/11/17 19:31
def money(a, b, c):
    '''

    :param a: 本金
    :param b: 利率
    :param c: 月数
    :return:
    '''
    s = 0
    assert c >= 0
    for i in range(0, 1 + c):
        m = a * (1 + b) ** i
        s = m + s

        print("第{}月本息{}".format(i,round(m,2)), round(s,2))

    return s


money(2000, 0.005, 5)
