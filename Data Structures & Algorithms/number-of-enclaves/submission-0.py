from collections import deque 
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def matrix_bfs(row, col, grid, visited):
            visited.add((row, col))
            queue = deque([(row, col)])
            DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
            ROWS = len(grid)
            COLS = len(grid[0])
            touched = False
            island_size = 0

            while queue:
                row, col = queue.popleft()
                island_size += 1

                for dr, dc in DIRECTIONS:
                    new_row, new_col = row + dr, col + dc 

                    if (0 > new_row or new_row >= ROWS) or (0 > new_col or new_col >= COLS):
                        touched = True
                    
                    elif (0 <= new_row and new_row < ROWS) and (0 <= new_col and new_col < COLS):
                        if (new_row, new_col) not in visited and grid[new_row][new_col] ==1:
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col))

            return island_size, touched

        
        visited = set()
        result = 0
        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == 1:
                    
                    size, touched = matrix_bfs(row, col, grid, visited)
                    if not touched:
                        result += size

        return result