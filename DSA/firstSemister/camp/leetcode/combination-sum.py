class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        def backtrack(sm,start):
            nonlocal result, curr
            if sm > target:
                return
            if sm == target:
                temp = sorted(curr)
                if temp not in result:
                    result.append(temp)
            for i in range(start,len(candidates)):
                curr.append(candidates[i])
                backtrack(sm + candidates[i],i)
                curr.pop()
            return 
        backtrack(0,0)
        return result