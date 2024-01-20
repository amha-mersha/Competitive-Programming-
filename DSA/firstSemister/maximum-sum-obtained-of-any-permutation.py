class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        queries = [0 for i in range(len(nums))]
        for start,end in requests:
            queries[start] += 1
            if end < len(nums)-1:
                queries[end+1] -= 1
        for i in range(1,len(queries)):
            queries[i] += queries[i-1]
        queries.sort(reverse = True)
        nums.sort(reverse = True)
        tot = 0
        for i in range(len(nums)):
            tot += nums[i] * queries[i]
        return tot % (10 ** 9 + 7)