class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def remove(self, item):
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

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.data == item:
                found = True
            else:
                if current.data > item:
                    stop = True
                else:
                    current = current.next
        return found

    def add(self, item):
        previous = None
        current = self.head
        stop = False
        while current != None and not stop:
            if current.data > item:
               stop = True
            else:
               previous = current
               current = current.next
        node = Node(item)
        if previous == None:
            node.next = self.head
            self.head = node
        else:
            node.next = current
            previous.next = node
