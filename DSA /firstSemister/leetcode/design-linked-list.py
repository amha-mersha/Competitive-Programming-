class Node:
    def __init__(self,val,next,prev):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.dummy = Node(None,self.head,None)

    def get(self, index: int) -> int:
        curr = self.head
        count = 0
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_head = Node(val,self.head,self.dummy)
        self.dummy.next = new_head
        if self.head:
            self.head.prev = new_head
        self.head = new_head

    def addAtTail(self, val: int) -> None:
        curr = self.dummy
        while curr and curr.next:
            curr = curr.next
        curr.next = Node(val,None,curr)
        if curr == self.dummy:
            self.head = curr.next

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.dummy
        count = 0
        while curr and curr.next:
            if count == index:
                new_node = Node(val,curr.next,curr)
                curr.next.prev = new_node
                curr.next = new_node
                if count == 0:
                    self.head = new_node
                    self.dummy.next = new_node
                    return 
            count += 1
            curr = curr.next
        if count == index:
            if curr == self.dummy:
                self.head = Node(val,None,self.dummy)
                self.dummy.next = self.head
            else:
                curr.next = Node(val,None,curr)
        return 

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        count = 0
        if index == 0:
            self.dummy.next = self.head.next
            if self.head.next:
                self.head.next.prev = self.dummy
            self.head = self.head.next
            return
        while curr:
            if count == index:
                curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                return 
            count += 1
            curr = curr.next
        return 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)