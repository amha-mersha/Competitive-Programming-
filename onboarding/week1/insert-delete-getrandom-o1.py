class RandomizedSet:

    def __init__(self):
        self.randomSet = set() 

    def insert(self, val: int) -> bool:
        if val not in self.randomSet:
            self.randomSet.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.randomSet:
            return False
        else:
            self.randomSet.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice(list(self.randomSet))        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()