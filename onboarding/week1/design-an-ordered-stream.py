class OrderedStream:

    def __init__(self, n: int):
        self.order = [0]*n
        self.ptr = 1
        self.last = 1
    def insert(self, idKey: int, value: str) -> List[str]:
        self.order[idKey-1] = value
        self.last = self.ptr
        while self.ptr <= len(self.order) and self.order[self.ptr-1] != 0 :
            self.ptr += 1
        return self.order[self.last-1:self.ptr-1]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)