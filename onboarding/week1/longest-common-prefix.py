class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        shortest = min(strs,key = len)
        for i,c in enumerate(shortest):
            for others in strs:
                if  c != others[i]:
                    return shortest[:i]
        return shortest 

        