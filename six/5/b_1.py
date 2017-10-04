# -*- coding:utf-8 -*-

def cmpstring():
    '''判断两个字符串是否一致'''
    str1 = raw_input("请输入一串字符1--->")
    str2 = raw_input("请输入一串字符2--->")

    if len(str1)!= len(str2):
        print "两个字符串不一致"
    else:
        for i in xrange(len(str1)):
            if str1[i] != str2[i]:
                print "不一致"
                break
        else:
            print "一致"

if __name__ == '__main__':
    cmpstring()
