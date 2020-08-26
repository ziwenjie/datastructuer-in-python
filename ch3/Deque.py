from pythonds.basic.deque import Deque
# 双端队列

def palcheker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual

print(palcheker('lslsslsl'))
print(palcheker('radar'))