class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        count = 0
        r = 0
        for l in range(len(g)):
            curr = 0
            while r < len(s) and curr < g[l]:
                curr = s[r]
                r += 1
            if curr >= g[l]:
                count += 1
                # r+=1
            else:
                break
        return count

        