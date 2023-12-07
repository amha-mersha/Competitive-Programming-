class Solution(object):
    def pivotArray(self, nums, pivot):
        pref = []
        pcount = 0
        suf = []
        for i in nums:
            if i < pivot:
                pref.append(i)
            elif i == pivot:
                pcount += 1
            else:
                suf.append(i)
        return pref + [pivot]*pcount + suf

        