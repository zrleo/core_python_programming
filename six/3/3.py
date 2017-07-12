# -*- coding:utf-8 -*-

'''
排序，
（a）输入一串数字，并从大到小排列之
（b）跟a一样，不过要用字典序从大到小排列
'''


def order():
    newlist = []
    nlist = raw_input("请输入")
    for x in nlist:
        newlist.append(int(x))
    return sorted(newlist, reverse=True)


if __name__ == '__main__':
    print order()

