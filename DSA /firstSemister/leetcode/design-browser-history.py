class Node:
    def __init__(self,val = None, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
       self.curr = Node(homepage) 

    def visit(self, url: str) -> None:
        new_page = Node(url)
        self.curr.next = new_page
        new_page.prev = self.curr
        self.curr = new_page

    def back(self, steps: int) -> str:
        count = 0
        while self.curr and self.curr.prev:
            self.curr = self.curr.prev
            count += 1
            if count == steps:
                return self.curr.val
        return self.curr.val

    def forward(self, steps: int) -> str:
        count = 0
        while self.curr and self.curr.next:
            self.curr = self.curr.next
            count += 1
            if count == steps:
                return self.curr.val
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)