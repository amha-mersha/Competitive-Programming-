# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = defaultdict(int)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root):
            if not root:
                return 
            self.count[root.val] += 1
            helper(root.left)
            helper(root.right)
            return 
        helper(root)
        mx = 0
        lst = []
        for i in self.count:
            if self.count[i] == mx:
                lst.append(i)
            elif self.count[i] > mx:
                lst = [i]
                mx = self.count[i]
        return lst