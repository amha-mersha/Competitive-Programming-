class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.lastMinute = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.lastMinute[tokenId] = currentTime + self.timeToLive
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.lastMinute and self.lastMinute[tokenId] > currentTime:
            self.lastMinute[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for i in self.lastMinute:
            if self.lastMinute[i] > currentTime:
                count += 1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)