from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def multi_bfs(grid):
            queue = deque()
            DIRECTIONS = [(1,0), (-1,0), (0,-1), (0,1)]
            ROWS = len(grid)
            COLS = len(grid[0])

            # populate grid w/ 0
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == 0:
                        grid[row][col] = 0
                        queue.append((row,col))
            
            # Do multi-source BFS 
            while queue:
                row, col = queue.popleft()
                if grid[row][col] == -1:
                    continue 
                
                for dr, dc in DIRECTIONS:
                    new_row, new_col = row+dr, col+dc
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 2**31 - 1:
                        queue.append((new_row, new_col))
                        
                        grid[new_row][new_col] = grid[row][col] + 1
        multi_bfs(grid)
            






