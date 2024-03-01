class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        curr = []
        
        def backtrack(idx,count, tot):
            nonlocal result, curr
            if tot >= n or count == k:
                if tot == n and count == k:
                    result.append(curr.copy())
                return 
            for i in range(idx,10):
                curr.append(i)
                backtrack(i+1,count + 1, tot+i)
                curr.pop()
            return 
        backtrack(1,0,0)
        return result