class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        tracker = set(nums)
        unique = len(tracker)
        l = 0
        count = 0
        counter = Counter()
        for r in range(len(nums)):
            counter[nums[r]] += 1 
            while len(counter) == unique: 
                counter[nums[l]] -= 1 
                if counter[nums[l]] == 0: 
                    del counter[nums[l]] 
                l += 1 
                count += len(nums) - r
        return count                                  