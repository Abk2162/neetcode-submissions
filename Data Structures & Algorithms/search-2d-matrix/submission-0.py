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

        l1, r1 = 0, m - 1
        while l1 <= r1:
            mid1 = (l1 + r1)//2

            if matrix[mid1][0] <= target <= matrix[mid1][n-1]:
                l2, r2 = 0, n - 1
                while l2 <= r2:
                    mid2 = (l2 + r2)//2
                    if target == matrix[mid1][mid2]:
                        return True
                    elif target > matrix[mid1][mid2]:
                        l2 = mid2 + 1
                    else:
                        r2 = mid2 - 1
                return False

            elif target > matrix[mid1][0]:
                l1 = mid1 + 1
            
            else:
                r1 = mid1 - 1
        return False

