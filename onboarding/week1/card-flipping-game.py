class Solution(object):
    def flipgame(self, fronts, backs):
        dontPick = set()
        res = float('inf')
        for i,j in zip(fronts,backs):
            if i == j:
                dontPick.add(i)
        for i in (fronts + backs):
            if i not in dontPick:
                res = min(res,i)
        return res if res!= float('inf') else 0

        