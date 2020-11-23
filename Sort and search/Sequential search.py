def sequentaiSearch(alist, item):
    """无序表查找"""
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found


testlist = [17, 20, 26, 31, 44, 54, 55, 65, 77]


def sequentaiSearch2(alist, item):
    """无序表查找"""
    found = False

    for i in range(len(alist)):
        if alist[i] == item:
            found = True
            break
    return found


def orderSearch(alist, item):
    """有序表搜索"""
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            return True
        elif alist[pos] > item:
            break
        else:
            pos += 1
    return found


def binarySearch(alist, item):
    """二分搜索"""
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def binarySearch2(alist, item):
    """二分搜索递归方法"""
    if len(alist) == 0:  # 结束条件
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:  # 缩小规模
                return binarySearch2(alist[: midpoint], item)  # 调用自身
            else:
                return binarySearch2(alist[midpoint + 1: ], item)


def bubbleSort(alist):
    """冒泡排序"""
    for passnum in range(len(alist) - 1, 0, -1):  # 多少趟（从n-1开始一直到1）
        for i in range(passnum):  # 比较第i位与第i + 1位两个元素的大小
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]  # 错序，交换


def shortBubbleSort(alist):
    """冒泡排序（性能改进）"""
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False  # 如果某一趟没有进行交换，则说明排序完成，结束循环
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum -= 1


def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location  # 在逆序的时候，只记录位置，并不交换
        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]  # 直到这一趟完成之后，再把最大项和最后一项的位置进行一次交换


alist = [2, 5, 3, 7, 9, 0]
selectionSort(alist)
print(alist)