def anagramSolution3(s1, s2):
    """异序词检测"""
    dic1 = {}
    dic2 = {}
    for i in s1:
        dic1[i] = dic1.get(i, 0) + 1
    for j in s2:
        dic2[j] = dic2.get(j, 0) + 1
    n = 0
    for m in dic1:
        try:
            if dic1[m] == dic2[m]:
                n += 1
        except:
            return False
    if n == len(dic1) == len(dic2):
        return True
    else:
        return False


def anagramSolution4(s1, s2):
    """异序词检测"""
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1
    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOK = False

    return stillOK


from timeit import Timer


def test1():
    """构造列表的方法"""
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")
print("+方法:", t1.timeit(number=1000))

t2 = Timer("test2()", "from __main__ import test2")
print("append方法:", t2.timeit(number=1000))

t3 = Timer("test3()", "from __main__ import test3")
print("列表推导式:", t3.timeit(number=1000))

t4 = Timer("test4()", "from __main__ import test4")
print("list方法:", t4.timeit(number=1000))


