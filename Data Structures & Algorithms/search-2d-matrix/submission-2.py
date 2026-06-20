class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])

        left = 0
        right = ROW * COL - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // COL
            col = mid % COL
            if matrix[row][col] == target:
                return True 
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False