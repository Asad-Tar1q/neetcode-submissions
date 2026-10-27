from collections import defaultdict

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        lo = 0
        hi = m * n - 1

        while hi >= lo:
            mid = (hi + lo) // 2
            i = mid // n
            j = mid % n
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                lo = mid + 1
            else:
                hi = mid - 1

            
        return False
        

