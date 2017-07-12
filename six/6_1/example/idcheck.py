#!usr/bin/env python
#-*- coding:utf-8 -*-

'''标识符合法性检查，规则：首先以字母或者下划线开始，后面跟字母、数字或者下划线'''
import string


alphas = string.letters + '_'
nums = string.digits

print '检验标志符的合法性，只检查长度大于2的标志符'
myInput = raw_input('Identifier to test?')

if len(myInput)>=1:
    if myInput[0] not in alphas:
        print '标志符不合法'
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print '不合法'

                break
                '''首位字符合法，但后续字符一旦出现不合法的字符，自动跳出循环，否则会判断每一个字符，遇到合法字符，仍然判断为合法
                故需要加break'''
        else:
            print 'ok'

