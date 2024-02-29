# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level_width = defaultdict(list)
        mx_width = 0
        def tree(root,row,col):
            nonlocal level_width
            if not root:
                return 
            if level_width[row]:
                level_width[row][0] = min(level_width[row][0],col)
                level_width[row][1] = max(level_width[row][1],col)
            else:
                level_width[row].append(col)
                level_width[row].append(col)
            tree(root.left,row+1,col*2-1)
            tree(root.right,row+1,col*2)
            return 
        tree(root,0,1)
        for i in level_width:
            mx_width = max(mx_width,level_width[i][1]-level_width[i][0]+1)
        return mx_width