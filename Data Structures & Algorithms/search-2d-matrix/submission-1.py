class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        if target < matrix[0][0]:
            return False
        elif target > matrix[m-1][n-1]:
            return False
        
        l = 0
        r = (m * n) - 1
        while l <= r:
            mid = (l + r) // 2
            mid_val = matrix[mid // n][mid % n]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return False