class Solution(object):
    def dividePlayers(self, skill):
        if (sum(skill)*2)%len(skill) != 0:
            return -1
        skill.sort()
        target = (sum(skill)*2)//len(skill)
        l,r = 0,len(skill)-1
        pair = 0
        while l < r:
            if skill[l] + skill[r] != target:
                return -1
            pair += (skill[l]*skill[r])
            l += 1
            r -= 1
        return pair
