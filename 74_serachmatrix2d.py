# serachmatrix2d-74.py
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix[0] or not matrix[0][0]:
            return False
        if matrix[0][0] == target:
            return True

        m = len(matrix)
        n = len(matrix[0])

        if matrix[m-1][n-1] < target:
            return False
        elif matrix[m-1][n-1] == target:
            return True
        
        lo, hi = 0, m * n -1
        while lo <= hi:
            mid = (lo + hi)//2
            x = mid // n
            y = mid % n
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
