class Solution:
    # def increasingTriplet(self, nums):
    #     first = second = float('inf') 
    #     for n in nums: 
    #         if n <= first: 
    #             first = n
    #         elif n <= second:
    #             second = n
    #         else:
    #             return True
    #     return False
    def increasingTriplet(self, nums):
        d = {i:float('inf') for i in range(2)}
        for n in nums: 
            for i in d:
                if d[i] >= n:
                    d[i] = n
                    break
            else:
                return True
        return False