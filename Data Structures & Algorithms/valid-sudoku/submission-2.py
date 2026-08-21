class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """

        9x9 sudoku `board`

        valid if the following rules are applied: 

        1. eaxch row must contain 1-9 | no duplicates
        2. each col must contain 1-9 | no duplicates
        3. each of the 9 3x3 subboxes must contain digits 1-9 no duplicates 

        APPOROACH
        1. create a row set, col set, and 9 3x3 box sets 
        2. iterate through each row and confirm if valid 
        3. iterate htrough each column and confirm if valid 
        4. confirm if the boxes by doing (row, col) then (row+col) // 9
        """
        
       
        boxes = [set() for _ in range(9)]

        # iterate through each rows 
        for row in range(len(board)):
            rows = set()
            for col in range(len(board[0])):
                if board[row][col] in rows:
                    return False 
                if board[row][col] != ".":
                    rows.add(board[row][col])
        
        for col in range(len(board[0])):
            cols = set()
            for row in range(len(board)):
                if board[row][col] in cols:
                    return False 
                if board[row][col] != ".":
                    cols.add(board[row][col])
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                idx = (row//3) * 3 + (col//3)
                if board[row][col] in boxes[idx]:
                    return False 
                if board[row][col] != ".":
                    boxes[idx].add(board[row][col])
        
        
        return True

    