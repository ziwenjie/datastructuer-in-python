# _*_ coding: utf-8 -*-
# @Time      : 8/24/20 4:58 PM
# @Author    : title_z
# @Filename  : BubbleSort.py


"""
O(n^2)
"""


def bubbleSort(alist):
    for passnum in range(len(alist) - 1):  # n-1趟
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                # temp = alist[i]    #交换次数
                # alist[i] = alist[i + 1]
                # alist[i + 1] = temp
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


def shortBubbleSort(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum -= 1


alist = [54, 65, 24, 31, 52, 56, 87, 95, 69]
shortBubbleSort(alist)
# bubbleSort(alist)
print(alist)
