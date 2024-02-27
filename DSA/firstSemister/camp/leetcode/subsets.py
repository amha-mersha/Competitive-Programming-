class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        def backtrack(idx):
            nonlocal result,curr
            if idx >= len(nums):
                result.append(curr.copy())
                return 
            backtrack(idx+1)
            curr.append(nums[idx])
            backtrack(idx+1)
            curr.pop()
            return 
        backtrack(0)
        return result