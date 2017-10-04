# -*- coding:utf-8 -*-


def scoreCalculate(score):
    if score < 60:
        rank = 'F'
    elif score < 70:
        rank = 'D'
    elif score < 80:
        rank = 'C'
    elif score < 90:
        rank = 'B'
    else:
        rank = 'A'
    return rank

scorelist = []
while True:
    myinput = raw_input("请输入分数：")
    print myinput
    if myinput == 'q':
        break
    else:
        scorelist.append(float(myinput))
average = sum(scorelist) / len(scorelist)
print average

