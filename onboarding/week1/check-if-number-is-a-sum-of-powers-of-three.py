class Solution:
    def checkPowersOfThree(self, n):
        while n:
            n, k = divmod(n,3)
            if k==2:
                return False
        return True
        