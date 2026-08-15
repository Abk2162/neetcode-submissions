# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if not node1:
                if node2:
                    return False
                continue
            if not node2:
                if node1:
                    return False
                continue
            if not node1 and not node2:
                continue

            if node1.val != node2.val:
                return False

            if node1.right: 
                stack1.append(node1.right)
            else:
                stack1.append(None)

            if node2.right:
                stack2.append(node2.right)
            else:
                stack2.append(None)

            if node1.left: 
                stack1.append(node1.left)
            else:
                stack1.append(None)

            if node2.left:
                stack2.append(node2.left)
            else:
                stack2.append(None)

        return True






