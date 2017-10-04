# -*- coding:utf-8 -*-

def stringstrip():
    str1 = raw_input("请输入一串字符串")
    print str1

    if str1[0] == ' ':
        if str1[-1] == ' ':
            str1 = str1[1:-1]
        else:
            str1 = str1[1:]
    elif str1[-1] == ' ':
        str1 = str1[0:-1]
    return str1

if __name__ == '__main__':
    print stringstrip()

