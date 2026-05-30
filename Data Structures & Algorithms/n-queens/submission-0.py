class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        temp = [["."] * n for _ in range(n)]
        diagonals = set()
        anti_diagonals = set()
        rows = set()

        def backtrack(col):
            if col == n:
                result.append(["".join(r) for r in temp])
                return 

            # Backtrack
            for row in range(n):
                if (row-col) in diagonals:
                    continue 
                if (row+col) in anti_diagonals:
                    continue 
                if row in rows:
                    continue 
                
                diagonals.add((row-col))
                anti_diagonals.add((row+col))
                rows.add(row)
                temp[row][col] = "Q"

                backtrack(col+1)
                diagonals.remove((row-col))
                anti_diagonals.remove((row+col))
                rows.remove(row)
                temp[row][col] = "."
            
        backtrack(0)
        return result


            
        

        