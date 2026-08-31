# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, l_limit, r_limit):
            if not node:
                return True
            
            if not (l_limit < node.val < r_limit):
                return False
                
            return (dfs(node.left, l_limit, node.val) and dfs(node.right, node.val, r_limit))
            
        return dfs(root, float('-inf'), float('inf'))