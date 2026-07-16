from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def multi_source(grid):
            ROWS = len(grid)
            COLS = len(grid[0])
            visited = [[-1] * COLS for _ in range(ROWS)]
            DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
            queue = deque()

            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == 2:
                        queue.append((row,col))
                        visited[row][col] = 0
            
            # start the multi)source bfs
            total_time = 0
            while queue:
                temp_len = len(queue)
    
                for _ in range(temp_len):
                    row,col = queue.popleft()

                    for dr, dc in DIRECTIONS:
                        new_row, new_col = row+dr, col+dc
                        if (0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 1 and visited[new_row][new_col] == -1):
                            visited[new_row][new_col] = 0
                            queue.append((new_row,new_col))
                total_time += 1
                
                
            return total_time, visited 
        result, visited =  multi_source(grid)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if visited[row][col] == -1 and grid[row][col] == 1:
                    return -1
        if result == 0:
            return result 
        return result-1

