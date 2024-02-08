class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        hashmap = {0:1}
        prefix = 0
        count = 0
        for i,item in enumerate(nums):
            prefix += item
            if prefix - goal in hashmap:
                count += hashmap[prefix-goal]
            hashmap[prefix] = hashmap.get(prefix,0) + 1
        return count