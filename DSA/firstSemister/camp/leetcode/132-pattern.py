class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        last = float('inf')
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] < nums[i]:
                last = stack.pop()
            stack.append(nums[i])
            if stack[0] > last > nums[i]:
                return True
        return False