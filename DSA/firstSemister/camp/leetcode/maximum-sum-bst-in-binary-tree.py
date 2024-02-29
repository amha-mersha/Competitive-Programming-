# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        mx = 0
        def helper(root):
            nonlocal mx
            if not root.right and not root.left:
                mx = max(mx,root.val)
                return True,root.val,root.val, root.val
            if not root.right and root.left:
                leftCondition,leftSum,leftMax,leftMin = helper(root.left)
                curr = 0    
                if leftCondition and leftMax < root.val:
                    curr += leftSum + root.val
                    mx = max(mx,curr)
                    return True, curr, max(root.val,leftMax,leftMin) , min(root.val,leftMax,leftMin)
                return False, curr,max(root.val,leftMax), min(root.val,leftMax)
            if root.right and not root.left:
                rightCondition, rightSum,rightMax,rightMin = helper(root.right)
                curr = 0    
                if rightCondition and rightMin > root.val:
                    curr += rightSum + root.val
                    mx = max(mx,curr)
                    return True, curr, max(rightMax,root.val,rightMin),min(rightMax,root.val,rightMin)
                return False, curr, max(root.val,rightMin),min(root.val,rightMin)
            leftCondition,leftSum,leftMax,leftMin = helper(root.left)
            rightCondition, rightSum,rightMax,rightMin = helper(root.right)
            curr = 0
            if leftCondition and rightCondition and leftMax < root.val and rightMin > root.val:
                curr += leftSum + rightSum + root.val
                mx = max(mx,curr)
                return True, curr, max(rightMax,leftMin,root.val,leftMax,rightMin),min(rightMax,leftMin,root.val,leftMax,rightMin)
            return False, curr, max(rightMax,leftMin,root.val,leftMax,rightMin),min(rightMax,leftMin,root.val,leftMax,rightMin)
        helper(root)
        return mx