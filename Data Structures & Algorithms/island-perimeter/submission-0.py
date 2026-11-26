class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        l = len(grid)
        b = len(grid[0])
        perimeter = 0
        for row, value in enumerate(grid):
            for col in range(len(value)):
                if grid[row][col] == 1:
                    perimeter += 4
                    if (row - 1) > -1:
                        if grid[row-1][col] == 1:
                            perimeter -= 1
                    if (row + 1) < l:
                        if grid[row+1][col] == 1:
                            perimeter -= 1
                    if (col - 1) > -1:
                        if grid[row][col-1] == 1:
                            perimeter -= 1
                    if (col + 1) < b:
                        if grid[row][col+1] == 1:
                            perimeter -= 1
        return perimeter
                
                