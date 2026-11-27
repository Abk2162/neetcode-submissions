"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        stack = []
        visit = dict()

        def dfs(node):
            if not node:
                return None
            if node.val in visit:
                return visit[node.val]

            new = Node(node.val)
            visit[node.val] = new

            for val in node.neighbors:
                temp = dfs(val)
                if temp:
                    new.neighbors.append(temp)
            
            return new

        return dfs(node)
