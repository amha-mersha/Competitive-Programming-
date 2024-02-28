class Node:
    def __init__(self,val =None,next = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.count < self.size:
            if not self.head:
                self.head = self.tail = Node(value)
            else:
                self.tail.next = Node(value)
                self.tail = self.tail.next
            self.count += 1
            return True
        return False
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head = self.head.next
            self.count -= 1
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.head.val
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        if not self.head:
            return True
        return False

    def isFull(self) -> bool:
        if self.count == self.size:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()