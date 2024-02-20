class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lgth = len(temperatures)
        ans = [0] * lgth
        stack = []
        for i in range(lgth):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                ans[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
        return ans