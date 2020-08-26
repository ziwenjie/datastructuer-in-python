# _*_ coding: utf-8 -*-
# @Time      : 8/22/20 10:23 AM
# @Author    : title_z
# @Filename  : recDC.py

def recDC(coinvaluelist, change, knownresults):
    mincoins = change
    if change in coinvaluelist:  # 递归基本结束条件
        knownresults[change] = 1  # 记录最优解
        return 1
    elif knownresults[change] > 0:  # 查表成功，直接用最优解
        return knownresults[change]  # 查表成功,直接最优解
    else:
        for i in [c for c in coinvaluelist if c <= change]:
            numcoins = 1 + recDC(coinvaluelist, \
                                 change - i, knownresults)
            if numcoins < mincoins:
                mincoins = numcoins
                knownresults[change] = mincoins
    return mincoins


print(recDC([1, 5, 10, 25], 63, [0] * 64))
