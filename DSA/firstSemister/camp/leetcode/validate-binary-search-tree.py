# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], curr_mn = float('-inf') , curr_mx = float('inf')) -> bool:
        if not root:
            return True
        if root.val <= curr_mn or root.val >= curr_mx:
            return False
        return self.isValidBST(root.left,curr_mn,min(curr_mx,root.val)) and self.isValidBST(root.right,max(curr_mn, root.val),curr_mx)