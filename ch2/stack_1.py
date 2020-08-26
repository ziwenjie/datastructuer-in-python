import pythonds
from pythonds.basic.stack import Stack
# s = Stack()
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):  # last item
#         return self.items[len(self.items)-1]
#
#     def size(self):
#         return len(self.items)

s = Stack()

print(s.isEmpty())
s.push(4)  # append 4
s.push('dog')  # append 'dog'
print(s.peek())  # print s last item
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.size())