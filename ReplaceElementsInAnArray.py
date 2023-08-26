class Solution(object):
    def arrayChange(self, nums, operations):
        hashmap = {num : index for index,num in enumerate(nums)}
        for old, new in operations:
            hashmap[new] = hashmap[old]
            nums[hashmap[old]] = new
            del hashmap[old]

        return nums

class Solution(object):
    def arrayChange(self, nums, operations):
        hashmap = {}
        for old,new in reversed(operations):
            hashmap[old] = hashmap.get(new,new)
        for idx,val in enumerate(nums):
            if val in hashmap:
                nums[idx] = hashmap[val]
        
        return nums
