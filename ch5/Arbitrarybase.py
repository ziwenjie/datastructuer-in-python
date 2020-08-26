# _*_ coding: utf-8 -*-
# @Time      : 8/18/20 8:12 PM
# @Author    : title_z
# @Filename  : Arbitrarybase.py

def toStr(n ,base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

print(toStr(65, 12))