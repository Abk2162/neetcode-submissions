class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        m_area = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0  # Sink visited land in-place
            area = dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)
            return 1 + area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    m_area = max(m_area, dfs(r, c))

        return m_area