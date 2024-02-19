class RecentCounter:

    def __init__(self):
        self.requests = []
        self.left = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[self.left] < t-3000:
            self.left += 1
        return len(self.requests) - self.left


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)