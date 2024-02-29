class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        def helper(score,turn, l, r):
            if turn:
                if l == r:
                    return score + nums[r] >= 0
                return helper(score + nums[l],False,l+1,r ) or helper(score+nums[r],False,l,r-1)
            if l == r:
                return score - nums[r] >= 0
            return helper(score-nums[l],True,l+1,r) and helper(score-nums[r],True,l,r-1)
        return helper(0,True,0,len(nums)-1)