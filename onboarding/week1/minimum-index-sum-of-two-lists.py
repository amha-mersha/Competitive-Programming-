class Solution(object):
    def findRestaurant(self, list1, list2):
        d = {}
        shortest = len(max((list1,list2),key = len))*2
        res = []
        ln = float("inf")
        for i in range(len(list1)):
            d[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in d:
                if j + d[list2[j]] == ln:
                    res.append(list2[j])
                if j + d[list2[j]] < ln:
                    ln = j + d[list2[j]]
                    res = [list2[j]]
        return res

        