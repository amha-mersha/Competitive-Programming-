# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        mx = 0
        def helper(root,localmax,localmin):
            nonlocal mx
            if not root:
                return 0
            localmax = max(localmax,root.val)
            localmin = min(localmin,root.val)
            mx = max(mx,localmax-localmin)
            helper(root.left,localmax,localmin)
            helper(root.right,localmax,localmin)
            return 
        helper(root,root.val,root.val)
        return mx
