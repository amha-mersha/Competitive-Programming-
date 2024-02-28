class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        def backtrack(seen):
            nonlocal result, curr
            if  len(curr) == len(nums):
                result.append(curr[:])
                return 
            for i in nums:
                if i not in seen:
                    curr.append(i)
                    seen.add(i)
                    backtrack(seen)
                    curr.pop()
                    seen.remove(i)
            return 
        backtrack(set())
        return result