class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] += 1
        running = 0
        count = 0
        for i in nums:
            running += i
            if running - k in prefix:
                count += prefix[running-k]
            prefix[running] += 1
        return count
        