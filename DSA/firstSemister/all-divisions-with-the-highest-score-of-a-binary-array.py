
class Solution:
    def maxScoreIndices(self, nums):
        checker = [nums[0]]
        for i in range(1,len(nums)):
            checker.append(checker[i-1] + nums[i])
        d = defaultdict(list)
        for i in range(len(nums)+1):
            if i  == 0:
                curr = checker[-1]
            elif i == len(nums):
                curr = len(nums)- checker[-1]
            else:
                curr = (i - checker[i-1]) + (checker[-1] - checker[i-1])
            d[curr].append(i)
        return d[max(d.keys())]