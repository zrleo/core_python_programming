# -*- coding:utf-8 -*-


'''
闰年判断方法：
1、能被4整除，且不可以被100整除
2、能被400整除
'''


def check_year():
    year = int(raw_input("请输入年份："))
    if (year % 4 == 0) & (year % 100 != 0):
        print "%s 是闰年"%year
    elif year % 400 == 0:
        print "%s 是闰年"%year
    else:
        print "%s不是闰年"%year

check_year()
