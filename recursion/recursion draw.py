import turtle as t

def drawSpiral(linelen):
    """画螺旋线"""
    if linelen > 0:
        t.forward(linelen)
        t.right(90)
        drawSpiral(linelen - 10)
    t.done()


def tree(branch_len):
    """画分形树"""
    if branch_len > 5:  # 树干不太短，即递归结束条件
        t.forward(branch_len)  # 画树干
        t.right(20)  # 右倾斜20度
        tree(branch_len - 15)  # 递归调用，画右边小树，树干减15
        t.left(40)  # 向左回40度，即左倾20度
        tree(branch_len - 15)  # 递归调用，画左边小树
        t.right(20)  # 向右回20度，即回正
        t.backward(branch_len)  # 海龟退回原位置


def sier(degree, points):
    """degree: 画几阶的三角形  points: 字典，描绘了三角形的轮廓的坐标 ，分别在字典中用left,right,top表示"""
    colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]
    draw(points, colormap[degree])
    if degree > 0:
        sier(degree - 1, \
             {"left": points["left"], \
              "top": getMid(points["left"], points["top"]), \
              "right": getMid(points["left"], points["right"])})
        sier(degree - 1, \
             {"left": getMid(points["left"], points["top"]), \
              "top": points["top"], \
              "right": getMid(points["top"], points["right"])})
        sier(degree - 1, \
             {"left": getMid(points["left"], points["right"]), \
              "top": getMid(points["top"], points["right"]), \
              "right": points["right"]})


def draw(points, color):
    """按照坐标画等边三角形"""
    t.fillcolor(color)
    t.penup()
    t.goto(points["top"])
    t.pendown()
    t.begin_fill()
    t.goto(points["left"])
    t.goto(points["right"])
    t.goto(points["top"])
    t.end_fill()


def getMid(p1, p2):
    """求中点坐标"""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


points = {"left": (-200, -100), \
          "top": (0, 200), \
          "right": (200, -100)}
sier(5, points)
t.done()
