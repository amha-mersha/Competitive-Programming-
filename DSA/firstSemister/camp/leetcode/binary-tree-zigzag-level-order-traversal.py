# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.level = defaultdict(list)
        self.depth = 0
        self.count = 0
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(root):
            if not root:
                self.count = max(self.count,self.depth)
                self.depth -= 1
                return 
            self.depth += 1
            helper(root.right)
            self.level[self.depth].append(root.val)
            self.depth += 1
            helper(root.left)
            self.depth -= 1
            return 
        helper(root)
        res = []
        for i in range(self.count):
            if i%2 ==1:
                res.append(self.level[i])
            else:
                res.append(reversed(self.level[i]))
        return res
        