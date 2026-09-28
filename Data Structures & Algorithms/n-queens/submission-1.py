class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """
        n queens on an nxn chessboard. Such that no queens attack

        Q = queen
        . is emptyh space 


        APPORACH:
        Backtracking :D 

        have a set for rows and diagonas and antidiagolns. COLS should be fine as we pcae it there....

        at every step compute the thing and then add it in there etc
        """
        result = []
        cols = set()
        diagonals = set()
        anti_diagonals = set()

        def backtrack(row, arr):
            if row == n:
                result.append(["".join(r) for r in arr])
                return 
            for col in range(n):
                if col not in cols and row+col not in diagonals and row-col not in anti_diagonals:
                    cols.add(col)
                    diagonals.add(row+col)
                    anti_diagonals.add(row-col)
                    arr[row][col] = "Q"
                    backtrack(row+1, arr)
                    # backtrack 
                    cols.remove(col)
                    diagonals.remove(row+col)
                    anti_diagonals.remove(row-col)
                    arr[row][col] = "."
        backtrack(0, [["."] * n for _ in range(n)])
        return result