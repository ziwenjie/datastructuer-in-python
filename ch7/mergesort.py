# _*_ coding: utf-8 -*-
# @Time      : 8/26/20 4:04 PM
# @Author    : title_z
# @Filename  : mergesort.py

def mergesort(lst):
    # 递归结束的条件
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left = mergesort(lst[:middle])  # 左半部排好序
    right = mergesort(lst[middle:])  # 右半部排好序

    merge = []
    while left and right:
        if left[0] <= right[0]:
            merge.append(left.pop(0))
        else:
            merge.append(right.pop(0))

    merge.extend(right if right else left)
    return merge


lst = [0, 2, 5, 1, 6, 8, 4, 12, 29, 56, 24, 23, 20, 28]
merge = mergesort(lst)
print(merge)
