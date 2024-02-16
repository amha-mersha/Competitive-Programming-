class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        print(nums)
        l,r,count = 0,0,0
        lgth = len(nums)
        for i in range(lgth-2):
            r = lgth - 1
            l = i + 1
            while l < r:
                curr = nums[l] + nums[r] 
                if curr > nums[i]:
                    count += r-l
                    l += 1
                else:
                    r -= 1
        return count