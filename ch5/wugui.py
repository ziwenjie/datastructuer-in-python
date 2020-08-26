# _*_ coding: utf-8 -*-
# @Time      : 8/18/20 8:35 PM
# @Author    : title_z
# @Filename  : wugui.py

import turtle
t = turtle.Turtle()

# t.forward(1000)
# turtle.done()

# # 正方形
# for i in range(4):
#     t.forward(100)
#     t.right(90)

# turtle.done()

# 五角星

# t.pencolor('red')
# t.pensize(3)
#
# for i in range(5):
#     t.forward(200)
#     t.right(144)
# t.hideturtle()

def drawspiral(t, linelen):
    if linelen > 0:
        t.forward(linelen)
        t.right(90)
        drawspiral(t, linelen-3)

drawspiral(t, 120)

turtle.done()