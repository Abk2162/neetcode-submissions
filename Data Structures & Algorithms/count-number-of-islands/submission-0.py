class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visit = set()

        def dfs(i,j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == "0" or (i,j) in visit:
                return None
 
            visit.add((i,j))
            dfs(i,j + 1)
            dfs(i,j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)
            
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visit:
                    count += 1
                    dfs(r,c)

        return count