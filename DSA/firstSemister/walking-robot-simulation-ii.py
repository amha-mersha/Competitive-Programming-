class Robot:

    def __init__(self, width: int, height: int):
        self.width = width 
        self.height = height
        self.dir = "East"
        self.pos = [0,0]
    def step(self, num: int) -> None:
        total=((self.height+self.width-2)*2)
        num=num%total
        if num != 0:
            i = 0
            while i < num:
                if self.dir == "East":
                    if self.pos[0] == self.width-1:
                        num += 1
                        self.dir = "North"
                    else:
                        self.pos[0] += 1
                elif self.dir == "North":
                    if  self.height-1 == self.pos[1]:
                        num += 1
                        self.dir = "West"
                    else:
                        self.pos[1] += 1
                elif self.dir == "West":
                    if self.pos[0] == 0:
                        num += 1
                        self.dir = "South"
                    else:
                        self.pos[0] -= 1
                elif self.dir == "South":
                    if self.pos[1] == 0:
                        num += 1
                        self.dir = "East"
                    else:
                        self.pos[1] -= 1
                i += 1
        elif self.pos == [0,0] and self.dir=="East":
            self.dir = "South" 
    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()