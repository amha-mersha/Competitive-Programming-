class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] += 1
        runSum = 0
        count = 0
        for i in nums:
            runSum += i
            if runSum - k in prefix:
                count += prefix[runSum-k]
            prefix[runSum] += 1
        return count
        