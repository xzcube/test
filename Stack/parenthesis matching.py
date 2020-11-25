from pythonds.basic.stack import Stack


def parCheaker(symbolString):
    """括号匹配"""
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


def matches(opens, close):
    openers = "({["
    closers = ")}]"
    return openers.index(opens) == closers.index(close)


print(parCheaker("(({}))"))
print(parCheaker("((())))"))