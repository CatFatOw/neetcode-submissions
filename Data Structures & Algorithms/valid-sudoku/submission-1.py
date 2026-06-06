class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                box_idx = (row//3) * 3 + (col//3)
                value = board[row][col]
                if value == ".":
                    continue 
                
                if value in row_set[row] or value in col_set[col] or value in box_set[box_idx]:
                    return False 
                row_set[row].add(value)
                col_set[col].add(value)
                box_set[box_idx].add(value)
        return True
        