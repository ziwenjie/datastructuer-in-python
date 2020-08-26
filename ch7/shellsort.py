# _*_ coding: utf-8 -*-
# @Time      : 8/26/20 3:40 PM
# @Author    : title_z
# @Filename  : shellsort.py

def shellsort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print('After increments of size', sublistcount,
              'The list is', alist)
        sublistcount //= 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentvalue


print(shellsort([2, 5, 3, 6, 1, 10, 8, 9, 12, 15, 46, 58, 24]))
