class Solution(object):
    def findWinners(self, matches):
        winns = defaultdict(int)
        loses = defaultdict(int)
        for i,j in matches:
            winns[i] += 1
            loses[j] += 1
        answer = [[],[]]
        for i in loses:
            if loses[i] == 1:
                answer[1].append(i)
        for i in winns:
            if i not in loses:
                answer[0].append(i)
        answer[0].sort()
        answer[1].sort()
        return answer


        