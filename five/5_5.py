# -*- coding:utf-8 -*-

'''取一个任意小于 1 美元的金额，然后计算可以换成最少多少枚硬币。
硬币有 1 美分，5 美分，10 美分，25 美分四种。1 美元等于 100 美分。
举例来说，0.76 美元换算结果 应该是 3枚25美分，1枚1美分。类似76枚1美分，2枚25美分+2枚10美分+1枚5美分+1
枚 1 美分这样的结果都是不符合要求的'''


def change_money():

    money = eval(raw_input("请输入一个金额："))*100
    if money % 25 != 0:
        n1 = int(money / 25)
        a = money % 25  # 除于25的余数
        n2 = int(a / 10)  # 10美分对应的个数
        b = a % 10
        n3 = int(b / 5)
        c = b % 5
        n4 = int(c / 1)
        print "%s个25美分，%s个10美分，%s个5美分， %s个1美分"%(n1,n2,n3,n4)
change_money()
