class Solution(object):
    def numIdenticalPairs(self, nums):
        count = {}
        good_number = 0
        for i in nums:
            if i in count:
                if count[i] == 1:
                    good_number += 1
                else:
                    good_number += count[i]
                count[i] += 1
            else:
                count[i] = 1
        return good_number
