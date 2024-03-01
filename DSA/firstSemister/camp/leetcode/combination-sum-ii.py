class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        candidates.sort()
        def backtrack(idx, sm):
            nonlocal result, curr
            if idx == len(candidates) or sm >= target:
                if sm == target:
                    result.append(curr.copy())
                    return 
                return 
            for i in range(idx,len(candidates)):
                if i == idx or (i > idx and candidates[i-1] != candidates[i]):
                    curr.append(candidates[i])
                    backtrack(i+1,sm+candidates[i])
                    curr.pop()
            return 
        backtrack(0,0)
        return result