# _*_ coding: utf-8 -*-
# @Time      : 8/18/20 4:23 PM
# @Author    : tile_z
# @Filename  : recursiveSum.py

def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])   # 调用自身


output = listsum([2, 5, 6, 9])
print(output)