class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visit = set()
        c0,c1,c2 = 0,0,0

        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 0 or grid[r][c] == 2):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    c2 += 1
                if grid[r][c] == 1:
                    c1 += 1
                if grid[r][c] == 0:
                    c0 += 1
        
        if c1 == 0:
            return 0

        count = -1
        changed = 0
        while q:
            count += 1
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                changed += 1
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)


        if c1+c2 != changed:
            return -1

        return count