class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        def compare(a,b):
            if a+b > b+a:
                return -1
            else:
                return 1
        nums.sort(key = cmp_to_key(compare))
        return str(int("".join(nums)))