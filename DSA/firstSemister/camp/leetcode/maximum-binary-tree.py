# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        indexmap = {nums[i]: i for i in range(len(nums))}
        
        def helper(left, right):
            if left > right:
                return None
            
            max_index = max(range(left, right + 1), key=lambda i: nums[i])
            node = TreeNode(nums[max_index])
            
            node.left = helper(left, max_index - 1)
            node.right = helper(max_index + 1, right)
            
            return node
        
        return helper(0, len(nums) - 1)
