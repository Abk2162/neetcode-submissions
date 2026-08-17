# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []
        self.find_path(root, p, path1)
        self.find_path(root, q, path2)
        
        # CHANGE 1: Equalize the path lengths before popping
        while len(path1) > len(path2):
            path1.pop()
        while len(path2) > len(path1):
            path2.pop()
            
        # CHANGE 2: Pop simultaneously until we find the match
        while path1 and path2:
            v1 = path1.pop()
            v2 = path2.pop()
            
            if v1 == v2:
                return v1
                
        return root

    def find_path(self, root, target, path):
        if not root:
            return False
            
        # CHANGE 3: Append the actual node object, not root.val
        path.append(root)

        # CHANGE 4: Compare the node directly to the target node
        if root == target:
            return True
            
        if self.find_path(root.left, target, path) or self.find_path(root.right, target, path):
            return True
            
        path.pop()
        return False        