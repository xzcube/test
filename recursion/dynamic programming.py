import numpy as np


def sumMax1(arr, i):
    """数列求和问题（递归形式）"""
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    else:
        A = sumMax(arr, i - 2) + arr[i]
        B = sumMax(arr, i - 1)
        return max(A, B)


def sumMax2(arr):
    """数列求和问题（动态规划）"""
    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        A = opt[i - 2] + arr[i]
        B = opt[i - 1]
        opt[i] = max(A, B)
    return opt[-1]


def subset1(arr, i, S):
    """数列中是否存在和为S的组合（递归方法）"""
    if S == 0:
        return True
    elif i == 0:
        return arr[0] == S
    elif arr[i] > S:
        return subset1(arr, i - 1, S)
    else:
        A = subset1(arr, i - 1, S - arr[i])
        B = subset1(arr, i - 1, S)
        return A or B


arr = [3, 34, 4, 12, 5, 2]
def subset2(arr, S):
    """列表中是否存在和为S的组合（动态规划）"""
    sub = np.zeros((len(arr), S + 1), dtype=bool)
    sub[:, 0] = True
    sub[0, :] = False
    sub[0, arr[0]] = True
    for i in range(1, len(arr)):
        for s in range(1, S + 1):
            if arr[i] > s:
                sub[i, s] = sub[i - 1, s]
            else:
                A = sub[i - 1, s - arr[i]]
                B = sub[i - 1, s]
                sub[i, s] = A or B
    return sub[len(arr) - 1, S]


def dpChange(coinValueList, change):
    """找零问题（动态规划）"""
    minCoins = [0]*(change + 1)
    for cents in range(1, change + 1):   # 从一分开始到change逐个计算最少硬币数
        coinCost = float("inf")   # 初始化一个最大硬币数
        for j in [c for c in coinValueList if c <= cents]:   # 减去每个硬币，向后查找最少硬币数，同时记录总的最少数
            if minCoins[cents - j] + 1 < coinCost:
                coinCost = minCoins[cents - j] + 1
            minCoins[cents] = coinCost   # 得到当前的最少硬币数，记录到表中
    return minCoins[change]   # 循环结束，得到最优解


def dpChange2(coinValueList, change):
    """找零问题（动态规划）"""
    result = np.zeros((len(coinValueList) + 1, change + 1), dtype=int)
    result[0, :] = 100
    for i in range(1, len(coinValueList) + 1):
        for j in range(1, change + 1):
            if coinValueList[i - 1] > j:
                result[i, j] = result[i - 1, j]
            else:
                A = 1 + result[i, j - coinValueList[i - 1]]
                B = result[i - 1, j]
                result[i, j] = min(A, B)
    return result[i][j]

