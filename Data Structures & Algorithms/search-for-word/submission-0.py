from collections import defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_freq = defaultdict(int)
        for char in word:
            word_freq[char] += 1


        def dfs(row, col, visited, i):
            ROWS = len(board)
            COLS = len(board[0])
            DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

            if board[row][col] != word[i]:
                return False

            if i == len(word)-1:
                return True 


            visited.add((row, col))
            

            for dr, dc in DIRECTIONS:
                new_row, new_col = row + dr, col + dc 
                if 0<= new_row and new_row < ROWS and 0 <= new_col and new_col < COLS:
                    if (new_row, new_col) not in visited:
                        if dfs(new_row, new_col, visited, i+1):
                            return True
                        # Backtrack
            visited.remove((row, col))

        visited = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) not in visited:
                    if dfs(row, col, visited, 0):
                        return True 
        return False

       