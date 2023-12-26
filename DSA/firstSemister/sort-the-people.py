
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        curr = list(zip(names, heights))
        curr.sort(key=lambda x: x[1], reverse = True)
        res = [curr[i][0] for i in range(len(names))]
        return res
