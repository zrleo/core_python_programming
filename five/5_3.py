# -*- coding:utf-8 -*-


def change_score_to_char():

    try:
        score = int(raw_input("请输入成绩："))
        if 90 <= score <= 100:
            print "A"
        elif 80 <= score <= 89:
            print "B"
        elif 70 <= score <= 79:
            print "C"
        elif 60 <= score <= 69:
            print "D"
        else:
            print "F"
    except ValueError, e:
        print "s输入错误",e

if __name__ == "__main__":
    change_score_to_char()

