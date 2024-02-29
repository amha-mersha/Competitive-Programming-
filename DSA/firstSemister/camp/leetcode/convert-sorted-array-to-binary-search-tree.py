# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dc(left,right):
            if left > right:
                return None
            midpt = (right + left)//2
            leftside = dc(left,midpt-1)
            rightside = dc(midpt+1,right)
            curr = TreeNode(nums[midpt],leftside,rightside)
            return curr
        return dc(0,len(nums)-1)