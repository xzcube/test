def recMC(coinValueList, change):
    """找零问题的递归解法"""
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins


def reDC(coinValueList, change, knowResules):
    """找零问题的优化（记忆化）"""
    minCoins = change
    if change in coinValueList:
        knowResules[change] = 1     # 记录最优解
        return 1
    elif knowResules[change] > 0:   # 在递归调用之前，先查找表中是否已经有部分找零的最有解
        return knowResules[change]  # 如果有，直接返回最优解而不进行递归调用，如果没有，才进行递归调用
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + reDC(coinValueList, change - i, knowResules)
            if numCoins < minCoins:
                minCoins = numCoins
                # 找到最优解，记录到表中
                knowResules[change] = minCoins
    return minCoins


