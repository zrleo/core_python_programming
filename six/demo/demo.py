# -*- coding:utf-8 -*-

d = {}


def read_file(filename):
    f = open(filename, 'r')
    for line in f.readlines():

        key, value = line.split(" ")
        d[key] = value

    for key, value in d.items():
        print key + "=" + value
    f.close()

if __name__ == '__main__':
    read_file("1.txt")
