from pythonds.basic.stack import Stack
"""
order reversal
"""
# 的方式萨的卡拉斯四大宋江离开阿斯大赛
def parChecker(symbolString):
    s = Stack()
    balance = True
    index = 0
    while index < len(symbolString) and balance:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)       # append all '(' in stack
        else:
            if s.isEmpty():
                balance = False
            else:
                s.pop()
        index += 1
    if balance and s.isEmpty():       # all brackets match and s is empty
        return True
    else:
        return False

# result = parChecker('((())))')
# print(result)

def bracketmatch(symbolString):
    s = Stack()
    balance = True
    index = 0
    while index < len(symbolString) and balance:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)       # append all '(' in stack
        else:
            if s.isEmpty():
                balance = False
            else:
                top = s.pop()
                if not match(top, symbol):
                    balance = False
        index += 1
    if balance and s.isEmpty():       # all brackets match and s is empty
        return True
    else:
        return False

def match(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)

print(bracketmatch('{{([][])}()}'))