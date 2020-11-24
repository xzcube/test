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
    """选择排序"""
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location  # 在逆序的时候，只记录位置，并不交换
        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]  # 直到这一趟完成之后，再把最大项和最后一项的位置进行一次交换



def insertionSort(alist):
    """插入排序"""
    for index in range(1, len(alist)):
        currentvalue = alist[index]   # 新项/插入项
        position = index
        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position -= 1   # 比对，移动
        alist[position] = currentvalue   # 插入新项


def shellSort(alist):
    """希尔排序"""
    sublistcount = len(alist)//2   # 间隔设定
    while sublistcount > 0:
        for startposition in range(sublistcount):   # 子列表排序
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increments of size,", sublistcount, "The list is", alist)
        sublistcount = sublistcount//2   # 间隔缩小


def gapInsertionSort(alist, start, gap):
    """子列表排序（插入排序）"""
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


def mergSort(alist):
    """归并排序"""
    print("Splitting", alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[: mid]
        righthalf = alist[mid: ]

        mergSort(lefthalf)
        mergSort(righthalf)

        i, j, k = 0, 0, 0

        while i < len(lefthalf) and j < len(righthalf):
            # 拉链式交错，把左右半部从小到大归并到结果中
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            # 归并左半部分剩余项
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            # 归并右半部分剩余项
            alist[k] = righthalf[j]
            j += 1
            k += 1
    print("Merging", alist)


def merge_sort(lst):
    """归并排序的（更pythonic）"""
    # 递归结束条件
    if len(lst) <= 1:
        return lst

    # 分解问题，递归调用
    middle = len(lst)//2
    left = merge_sort(lst[middle:])   # 左半部分排好序
    right = merge_sort(lst[: middle])  # 右半部分派好序

    # 合并左右半部，完成排序
    merged = []
    while left and right:  # 当左右半部都有数据的时候进行合并
        if left[0] <= right[0]:  # 对比左右半部首部的数据，哪个小就把哪个添加到列表中
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(right if right else left)  # 将剩余还有数据的半部加到列表中
    return merged


def quicksort(alist):
    """快速排序"""
    quicesortHelper(alist, 0, len(alist) - 1)


def quicesortHelper(alist, first, last):
    """指定快速排序的开始和结尾"""
    if first < last:
        splitpoint = partition(alist, first, last)
        quicesortHelper(alist, first, splitpoint - 1)
        quicesortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    """分裂的函数"""
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while rightmark >= leftmark and alist[rightmark] >= pivotvalue:
            rightmark -= 1
        if leftmark > rightmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark


alist = [2, 11, 5, 3, 7, 8, 6, 1, 9]
quicksort(alist)
print(alist)