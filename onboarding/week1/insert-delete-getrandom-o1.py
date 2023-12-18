class RandomizedSet:

    def __init__(self):
        self.randomList = []
        self.randomDict = {}

    def insert(self, val: int) -> bool:
        if val not in self.randomDict:
            self.randomList.append(val)
            self.randomDict[val] = len(self.randomList) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.randomDict:
            return False
        else:
            ind = self.randomDict[val]
            self.randomList[ind] = self.randomList[-1]
            self.randomDict[self.randomList[-1]] = ind
            self.randomDict.pop(val)
            self.randomList.pop()
            return True

    def getRandom(self) -> int:
        return random.choice(self.randomList)        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()