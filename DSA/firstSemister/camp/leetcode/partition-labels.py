class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = defaultdict(int)
        for ind,itm in enumerate(s):
            hashmap[itm] = ind
        
        j = 0
        res = []
        while j < len(s):
            start = j
            end = hashmap[s[j]]
            while j <= end and j < len(s):
                end = max(end,hashmap[s[j]])
                j += 1
            res.append(j - start)
        return res