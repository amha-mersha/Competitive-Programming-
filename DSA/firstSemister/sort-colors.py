class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i,j,k = 0,0,len(nums)-1
        while j < k+1:
            if nums[j] == 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[k],nums[j] = nums[j],nums[k]
                k -= 1
        """
        Do not return anything, modify nums in-place instead.
        """
        