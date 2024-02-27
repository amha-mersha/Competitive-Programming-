class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr = []
        result = []
        def backtrack(idx):
            nonlocal curr, result
            if idx >= len(nums):
                if curr not in result:
                    result.append(curr.copy())
                return 
            backtrack(idx + 1)
            curr.append(nums[idx])
            backtrack(idx+1)
            curr.pop()
            return 
        backtrack(0)
        return result