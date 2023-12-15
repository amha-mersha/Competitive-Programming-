class Bitset:

    def __init__(self, size: int):
        self.bitset = [0]*size
        self.inverset = [1]*size
        self.get_count = 0
        self.size = size
    def fix(self, idx: int) -> None:
        if self.bitset[idx] == 0:
            self.get_count += 1
        self.bitset[idx] = 1
        self.inverset[idx] = 0

    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == 1:
            self.get_count -= 1
        self.bitset[idx] = 0
        self.inverset[idx] = 1

    def flip(self) -> None:
        self.get_count = self.size - self.get_count
        self.bitset,self.inverset = self.inverset,self.bitset

    def all(self) -> bool:
        return self.get_count == self.size

    def one(self) -> bool:
        return self.get_count > 0

    def count(self) -> int:
        return self.get_count

    def toString(self) -> str:
        return "".join(map(str,self.bitset))


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()