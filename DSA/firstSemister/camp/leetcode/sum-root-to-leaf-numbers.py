# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack = []
        self.sum = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.stack.append(str(root.val))
        if not root.right and not root.left:
            self.sum += int("".join(self.stack))
            self.stack.pop()
            return self.sum
        if not root.right:
            self.sumNumbers(root.left)
            self.stack.pop()
            return self.sum
            
        if not root.left:
            self.sumNumbers(root.right)
            self.stack.pop()
            return self.sum
        self.sumNumbers(root.left)
        self.sumNumbers(root.right)
        self.stack.pop()
        return self.sum