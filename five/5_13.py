# -*- coding:utf-8 -*-


def time(h, m):
    h = int(h)
    m = int(m)

    t = h * 60 + m
    return t

if __name__ == '__main__':

    s = raw_input("请按HH:MM格式输入时间")
    s = s.split(":")
    print time(s[0], s[1] )