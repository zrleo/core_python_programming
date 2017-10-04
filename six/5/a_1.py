# -*- coding:utf-8 -*-

str1 = raw_input("Enter a string -->")

for ch in str1:
    print ch,

print
print "reversed"
for ch in str1[::-1]:
    print ch,
