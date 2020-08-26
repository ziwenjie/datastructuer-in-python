# _*_ coding: utf-8 -*-
# @Time      : 8/22/20 9:09 AM
# @Author    : title_z
# @Filename  : movetower.py

def moveTower(height, frompole, withpole, topole):
    if height >= 1:
        moveTower(height - 1, frompole, topole, withpole)
        moveDisk(height, frompole, topole)
        moveTower(height - 1, withpole, frompole, topole)

def moveDisk(disk, frompole, topole):
    print(f"moving disk[{disk} from {frompole} to {topole}")

moveTower(10, "#1", "#2", "#3")