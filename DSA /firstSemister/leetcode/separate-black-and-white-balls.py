class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = 0
        zeros = 0
        for i in s:
            if i == "0":
                zeros += ones
            else:
                ones += 1
        return zeros