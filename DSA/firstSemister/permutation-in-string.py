class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        comp = [0]*26
        curr = [0]*26
        for i in range(len(s1)):
            comp[ord(s1[i])-97] += 1
            curr[ord(s2[i]) -97] += 1
        if curr == comp:
            return True
        for i in range(len(s2)-len(s1)):
            curr[ord(s2[i]) -97] -= 1
            curr[ord(s2[i+len(s1)]) -97] += 1
            if curr == comp:
                return True
        return False