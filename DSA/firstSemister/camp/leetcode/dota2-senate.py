class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        count = Counter(senate)
        stack = []
        removed = set()
        while count["R"] != 0 and count["D"] != 0:
            for i in range(n):
                if i in removed:
                    continue
                if stack and stack[-1] != senate[i]:
                    stack.pop()
                    count[senate[i]] -= 1
                    removed.add(i)
                    
                else:
                    stack.append(senate[i])
                if count["R"] == 0 or count["D"] == 0:
                    break
        return "Radiant" if count["R"] > count["D"] else "Dire"