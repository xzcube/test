def BinaryTree(r):
    """嵌套列表法实现二叉树"""
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootval(root):
    return root[0]


def setRootval(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


class BinaryTree2:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree2(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree2(newNode)
        else:
            t = BinaryTree2(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

r = BinaryTree2("a")
r.insertLeft("b")
r.insertRight("c")
r.getRightChild().setRootVal("hello")
r.getLeftChild().insertRight("d")
print(r.getRootVal())



"""
r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
print(r)
insertRight(r, 6)
print(r)
insertRight(r, 7)
print(r)
l = getLeftChild(r)
print(l)
setRootval(l, 9)
print(r)
m = getRightChild(getRightChild(r))
print(m)
tree = ["a", ["b", ["d", [], []], ["e", [], []]], ["c", ["f", [], []], []]]
"""