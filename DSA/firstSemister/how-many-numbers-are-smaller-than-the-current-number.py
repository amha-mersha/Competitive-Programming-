class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        comp = {}
        res = []
        copyNum = sorted(nums)
        for i in range(len(nums)):
            if copyNum[i] not in comp:
                comp[copyNum[i]] = i
        for i in nums:
            res.append(comp[i])
        return res
