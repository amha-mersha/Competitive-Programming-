class Solution(object):
    def reverse(self, x):
        reverse = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            digit = x % 10
            reverse = reverse * 10 + digit
            x /= 10
        result = sign * reverse
        if result > 2 ** 31 - 1 or result < -(2 ** 31):
            return 0
        return result
# not accepted by leetcode but worked on local machine 
"""import math
class Solution(object):
    def reverse(self, x):
        max = 2147483647
        min = -214483468
        result = 0
        while x:
            temp = int(math.fmod(x,10))
            x = int(x/10)
            if (result > (max//10) or (result == (max//10) and temp >= (max%10))):
                return 0
            if (result < (min//10) or (result == (min//10) and temp <= (min%10))):
                return 0
            result = (result*10) + temp
        return result """
