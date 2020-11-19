def toStr(n, base):
    converString = "0123456789ABCDEF"
    if n < base:
        return converString[n]
    else:
        return toStr(n // base, base) + converString[n % base]


print(toStr(1453, 16))