# _*_ coding: utf-8 -*-
# @Time      : 8/27/20 3:19 PM
# @Author    : title_z
# @Filename  : Binarytree.py

from pythonds.trees import BinaryTree

# r = BinaryTree(3)
# BinaryTree.insertLeft(r, 4)
# BinaryTree.insertLeft(r, 5)
# BinaryTree.insertRight(r, 6)
# BinaryTree.insertRight(r, 7)
# l = BinaryTree.getLeftChild(r)
# print(l)

r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
r.getRightChild().setRootVal('hello')
r.getLeftChild().insertRight('d')
print(r)