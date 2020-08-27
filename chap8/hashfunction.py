# _*_ coding: utf-8 -*-
# @Time      : 8/27/20 10:16 AM
# @Author    : title_z
# @Filename  : hashfunction.py

def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum % tablesize


astring = 'asdassdf'
result = hash(astring, 11)
print(result)
