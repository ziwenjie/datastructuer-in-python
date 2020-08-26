# _*_ coding: utf-8 -*-
# @Time      : 8/18/20 8:54 PM
# @Author    : title_z
# @Filename  : tree.py

import turtle
t = turtle.Turtle()

def tree(branch_len):
    if branch_len > 5: # 递归的条件
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15)
        t.left(40)
        tree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)

t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
tree(120)
t.hideturtle()
turtle.done()
