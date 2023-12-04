class Solution(object):
    def escapeGhosts(self, ghosts, target):
        gosts = []
        me = abs(target[0]) + abs(target[1])
        for i,j in ghosts:
            total = abs(target[0]-i) + abs(target[1]-j)
            gosts.append(total)
        if min(gosts) <= me:
            return False
        else:
            return True

        