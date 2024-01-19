class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1]
        backward = [1]
        for i in range(len(nums)):
            forward.append(forward[-1] * nums[i])
        for i in range(len(nums)-1,-1,-1):
            backward.append(backward[-1]*nums[i])
        backward = backward[::-1]
        res = []
        for i in range(len(nums)):
            res.append(forward[i]*backward[i+1])
        return res
# [1,1,2,6,24]
#   [1,2,3,4]
# [24,24,12,4,1]
