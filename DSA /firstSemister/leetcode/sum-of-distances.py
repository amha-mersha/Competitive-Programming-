class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        trackInd = defaultdict(list)
        for ind,itm in enumerate(nums):
            trackInd[itm].append(ind)
        res = [0] * len(nums)
        for itm,vals in trackInd.items():
            runSum = 0
            tot = sum(vals)
            for ind,num in enumerate(vals):
                runSum += num
                if ind > 0:
                    res[num] += num*ind - (runSum - num)
                if ind < len(vals) - 1:
                    res[num] += tot - runSum - (len(vals)-1-ind) * num
        return res