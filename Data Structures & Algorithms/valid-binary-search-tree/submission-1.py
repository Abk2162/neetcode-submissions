# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        def dfs(root, l_limit, r_limit):
            if root.left:
                if l_limit < root.left.val < root.val:
                    if not dfs(root.left, l_limit, root.val):
                        return False
                else:
                    return False 
            if root.right:
                if root.val < root.right.val < r_limit:
                    if not dfs(root.right, root.val, r_limit):
                        return False
                else:
                    return False 
            return True
        valid = dfs(root, float('-inf'), float('inf'))
        return valid