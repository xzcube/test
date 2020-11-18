class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None


class UnorderedList:
    def __init__(self, node=None):
        self.head = node

    def isEmpty(self):
        """判断链表是否为空"""
        if self.head == None:
            return True
        else:
            return False

    def length(self):
        """获得链表长度"""
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def travel(self):
        """遍历整个链表"""
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

    def append(self, item):
        """链表尾部添加节点（尾插法）"""
        node = Node(item)
        if self.isEmpty():
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def add(self, item):
        """链表头部添加元素（头插法）"""
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def insert(self, pos, item):
        """指定位置添加元素
        ：param pos坐标从零开始索引
        """
        node = Node(item)
        pre = self.head
        count = 0
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            while count < (pos - 1):
                pre = pre.next
                count += 1
            # 当循环退出后，pre指向pos-1位置
            node.next = pre.next
            pre.next = node

    def search(self, item):
        current = self.head
        while current != None:
            if current.data == item:
                return True
            else:
                current = current.next
        return False

    def remove1(self, item):
        pre = None
        current = self.head
        while current != None:
            if current.data == item:
                # 先判断此节点是否是头节点
                if current == self.head:
                    self.head = current.next
                else:
                    pre.next = current.next
            else:
                pre = current
                current = current.next

    def remove2(self, item):
        current = self.head
        pre = None
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                pre = current
                current = current.next
        if pre == None:
            self.head = current.next
        else:
            pre.next = current.next


ll = UnorderedList()
ll.add(8)
ll.add(5)
ll.add("dog")
ll.remove2(8)
ll.travel()