from pythonds.basic.stack import Stack

def divideBy(decNumber, n):
    digits = '0123456789ABCDEF'
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % n  #take the remainder
        remstack.push(rem)
        decNumber = decNumber // n # interger division

    binString = ""
    while not remstack.isEmpty():
        binString = binString + digits[remstack.pop()]  #the number is the place

    return binString

print(divideBy(60, 16))