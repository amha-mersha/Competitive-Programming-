class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        count = 0
        for ind, item in enumerate(nums):
            if item in d:
                for i in d[item]:
                    if (i*ind)%k == 0:
                        count += 1
            d[item].append(ind)
        return count