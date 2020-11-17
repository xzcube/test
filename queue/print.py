from pythonds.basic import Queue
import random


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印速度（按分钟来算）
        self.currentTask = None  # 打印任务
        self.timeRemaining = 0  # 任务倒计时（当前正在打印的任务还剩下多少时间）

    def starNext(self, newtask):  # 打印新作业
        self.currentTask = newtask
        self.timeRemaining = (newtask.getPages() * 60) / self.pagerate  # 乘60转化成打印所需的秒数

    def tick(self):  # 打印一秒
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):  # 打印忙？
        if self.currentTask != None:
            return True
        else:
            return False


class Task:
    def __init__(self, time):
        self.timestamp = time  # 生成时间戳

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        self.pages = random.randrange(1, 21)  # 打印页数
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp  # 等待时间



def newPrintTask():
    num = random.randrange(1, 181)  # 1/180概率生成作业
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.starNext(nexttask)
        labprinter.tick()
    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))


for i in range(10):
    simulation(3600, 5)