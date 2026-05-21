from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        """
        Use a multi-source BFS appraoch :D
        """

        def multi_source_bfs(grid):
            ROWS = len(grid)
            COLS = len(grid[0])
            DIRECTIONS = [(1,0), (-1,0), (0,-1), (0,1)]
            queue = deque()
            time = 0
            visited = set()
            


            for row in range(ROWS):
                for col in range(COLS):
                    # If rotten!
                    if grid[row][col] == 2:
                        queue.append((row, col))
                        visited.add((row, col))


            while queue:
                time += 1

                for _ in range(len(queue)):
                
                    row, col = queue.popleft()

                    for dr, dc in DIRECTIONS:
                        new_row, new_col = row+dr, col + dc
                        if 0 <= new_row and new_row < ROWS and 0 <= new_col and new_col < COLS:
                            if (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                                visited.add((new_row, new_col))
                                queue.append((new_row, new_col))
                                grid[new_row][new_col] = 2
                

                
            
            for row in range(ROWS):
                for col in range(COLS):
                    # IF FRESH STILL EXISTS
                    if grid[row][col] == 1:
                        return -1
            if time - 1 >= 0:
                return time - 1
            else:
                return 0
        return multi_source_bfs(grid)

                


