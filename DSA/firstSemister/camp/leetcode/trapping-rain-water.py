class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        traped = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                bottom = stack.pop()
                if stack:
                    level = stack[-1]
                    traped += (min(height[level],height[i])-height[bottom])*(i-level-1)
            stack.append(i)
        return traped