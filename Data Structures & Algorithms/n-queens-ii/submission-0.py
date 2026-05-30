class Solution:
    def totalNQueens(self, n: int) -> int:
        result = []
        temp = [["."] * n for _ in range(n)]

        diag = set()
        rows = set()
        anti_diag = set()
        def backtrack(col):
            if col == n:
                result.append(["".join(r) for r in temp])
                return 
            
            for row in range(n):
                if row - col in diag:
                    continue 
                if row + col in anti_diag:
                    continue 
                if row in rows:
                    continue 
                
                diag.add((row-col))
                anti_diag.add((row+col))
                rows.add(row)
                temp[row][col] = "Q" 
                backtrack(col+1)
                # undo everything :( 
                diag.remove((row-col))
                anti_diag.remove((row+col))
                rows.remove(row)
                temp[row][col] = "." 
        backtrack(0)
        return len(result)

        