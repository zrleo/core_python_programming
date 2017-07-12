# -*- coding:utf-8 -*-

'''计算营业税'''


def tax(a):
    tax = a * 0.8
    return tax

if __name__ == '__main__':
    a = input("请输入一个数字：")
    print tax(a)