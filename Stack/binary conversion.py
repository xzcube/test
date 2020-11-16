from pythonds.basic import Stack
def divideBy2(decNumber, base):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(Hexadecimal(rem))
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + str(remstack.pop())

    return newString, base

def Hexadecimal(rem):
    if rem > 9:
        hexa = chr(rem - 10 + 65)
        return hexa
    else:
        return rem

print(format(divideBy2(233, 16)))