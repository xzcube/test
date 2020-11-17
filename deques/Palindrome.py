from pythonds.basic import Deque

def palchecker(aString):
    charduque = Deque()

    for ch in aString:
        charduque.addRear(ch)

    stillEqual = True
    while charduque.size() > 1 and stillEqual:
        first = charduque.removeFront()
        last = charduque.removeRear()
        if first != last:
            stillEqual = False
            break

    return stillEqual

print(palchecker("shguah"))
print(palchecker("reaer"))