# _*_ coding: utf-8 -*-
# @Time      : 8/24/20 4:31 PM
# @Author    : title_z
# @Filename  : binarySearch.py

def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        mid = (first + last)
        if alist[mid] == item:
            found = True
        else:
            if item < alist[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


def recursivebinarysearch(alist, item):
    if len(alist) == 1 and item not in alist:  # 当alist中只有唯一一项时，item是否相等
        return False
    else:
        mid = len(alist) // 2  # 向下取整
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return recursivebinarysearch(alist[:mid], item)
            else:
                return recursivebinarysearch(alist[mid:], item)


testlist = [0, 1, 2, 8, 13, 16, 20, 45, 56, 89, 90, 92, 95]
print(binarySearch(testlist, 56))
print(recursivebinarysearch(testlist, 95))
