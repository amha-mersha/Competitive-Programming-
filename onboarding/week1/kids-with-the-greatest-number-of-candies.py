class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        top = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= top:
                result.append(True)
            else:
                result.append(False)
        return result
        