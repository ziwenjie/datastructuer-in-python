# _*_ coding: utf-8 -*-
# @Time      : 8/22/20 10:02 AM
# @Author    : title_z
# @Filename  : changecoin.py

def recMC(coinValuelsit, change):
    minCoins = change
    if change in coinValuelsit:
        return 1
    else:
        for i in [c for c in coinValuelsit if c <= change]:
            numCoins = 1 + recMC(coinValuelsit, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

print(recMC([1, 5, 10, 25], 63))