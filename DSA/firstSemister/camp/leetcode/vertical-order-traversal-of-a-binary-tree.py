from collections import defaultdict
from typing import List, Optional

class Solution:
    def __init__(self):
        self.hashmap = defaultdict(list)
        self.min = float('inf')
        self.max = float('-inf')
        
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(root, location=0, row=0):
            if not root:
                self.min = min(self.min, location)
                self.max = max(self.max, location)
                return

            self.hashmap[location].append((row, root.val))
            helper(root.left, location - 1, row + 1)
            helper(root.right, location + 1, row + 1)

        helper(root)
        res = []
        for i in range(self.min+1, self.max):
            temp = [val for row, val in sorted(self.hashmap[i])]
            res.append(temp)

        return res
