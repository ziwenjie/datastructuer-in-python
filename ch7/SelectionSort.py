# _*_ coding: utf-8 -*-
# @Time      : 8/26/20 3:18 PM
# @Author    : title_z
# @Filename  : SelectionSort.py

def selectionsort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        postionofmax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[postionofmax]:
                postionofmax = location

        alist[fillslot], alist[postionofmax] = alist[postionofmax], alist[fillslot]


alist = [2, 3, 6, 4, 25, 8, 56, 62, 64, 87, 98, 63]
selectionsort(alist)
print(alist)
