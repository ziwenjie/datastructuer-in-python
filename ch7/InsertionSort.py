# _*_ coding: utf-8 -*-
# @Time      : 8/26/20 3:26 PM
# @Author    : title_z
# @Filename  : InsertionSort.py

def insertionsort(alist):
    for index in range(1, len(alist)):
        # 插入新项
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:  # 找比他小的数
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


alist = [2, 3, 6, 5, 8, 4, 10, 20, 13, 15, 12, 25, 20]
insertionsort(alist)
print(alist)
