# -*- coding:utf-8 -*-

import random


def demo():
    num = random.randint(1, 100)
    all = []
    for i in range(num):
        temp = random.randint(1, pow(2, 31)-1)
        all.append(temp)
        all.sort()
    return all


if __name__ == '__main__':
    print demo()