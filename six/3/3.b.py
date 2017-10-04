# -*- coding:utf-8 -*-

'''
注意：字典序就是按字典的排列方式，比如21就大于111，因为2大于1方式就是把输入的数字变成字符串即可,
优先比较首字母
'''


str1 = raw_input("Enter some numbers -->").split()
ltnum = []
for ch in str1:
    ltnum.append(int(ch))
lt2 = sorted(ltnum)[::-1]


ltDict = []
for ch in str1:
    ltDict.append(ch)
ltDict2 = sorted(ltDict)[::-1]
print lt2
print ltDict2
