class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        track = [0] * k
        track[0] = 1
        runSum = 0
        res = 0
        for i,item in enumerate(nums):
            runSum += item
            res += track[(runSum%k)]
            track[runSum%k] += 1
        return res
        
        