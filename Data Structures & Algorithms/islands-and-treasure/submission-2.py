from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c,0))

        while q:
            r,c,val = q.popleft()
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == -1 or (r,c) in visit:
                continue
            if grid[r][c] > val:
                grid[r][c] = val
            visit.add((r,c))
            q.append((r-1,c,val+1))
            q.append((r+1,c,val+1))
            q.append((r,c-1,val+1))
            q.append((r,c+1,val+1))
        