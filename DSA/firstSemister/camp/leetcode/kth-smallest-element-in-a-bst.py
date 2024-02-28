# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.track = 0
        self.result = -1
        def search(root):
            if not root:
                return 
            if root.left:
                search(root.left)
            self.track += 1
            if self.track == k:
                self.result = root.val
            if root.right:
                search(root.right)
            return 
        search(root)
        return self.result