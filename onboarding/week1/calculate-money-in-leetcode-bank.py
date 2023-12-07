class Solution(object):
    def totalMoney(self, n):
        weeks = n // 7
        days = n % 7
        res = 28*weeks + int(((weeks)*(7*(weeks-1)))/2) + int(((days)*(2*(weeks + 1) + (days-1)))/2)
        return res

        