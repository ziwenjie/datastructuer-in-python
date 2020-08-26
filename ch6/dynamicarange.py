# _*_ coding: utf-8 -*-
# @Time      : 8/22/20 10:59 AM
# @Author    : title_z
# @Filename  : dynamicarange.py

def dpmakechange(coinvaluelist, change, mincoins):
    for cents in range(1, change + 1):
        coincount = cents
        for j in [c for c in coinvaluelist if c <= cents]:
            if mincoins[cents - j] + 1 < coincount:
                coincount = mincoins[cents - j] + 1
        mincoins[cents] = coincount
    return mincoins[change]


print(dpmakechange([1, 5, 10, 21, 25], 63, [0] * 64))
