# -*- coding:utf-8 -*-


def rate(s_rate):
    day_rate = float(s_rate)
    year_rate = (1+day_rate)*365-1
    return "Annual return is %f" % year_rate

if __name__ == '__main__':
    s_rate = raw_input("输入日利率：")
    print rate(s_rate)