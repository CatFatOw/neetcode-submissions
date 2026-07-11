from collections import deque 
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        def bfs(start, visited):
            queue = deque([start])
            visited.add(start)
            DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
            ROWS = len(grid)
            COLS = len(grid[0])
            islands= []

            while queue:
                row, col = queue.popleft()
                islands.append((row,col))

                for dr, dc in DIRECTIONS:
                    new_row, new_col = row+dr, col+dc 
                    if (0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))

            return islands 
        
        # Find the islands, then start multi-source BFS on those cells and stop at the first 1
        visited = set()
        row = None 
        col = None 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    row = r
                    col = c
                    break
            if grid[r][c] == 1:
                break

        islands = bfs((row, col), visited)
        

        def multi_source_bfs(grid):
            ROWS = len(grid)
            COLS = len(grid[0])
            DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
            count = 0
            queue = deque()
            result = [[-1] * COLS for _ in range(ROWS)]

            # Put all cells in islands into result 
            for row in range(ROWS):
                for col in range(COLS):
                    if (row, col) in islands:
                        result[row][col] = 0
                        queue.append((row,col))
            # BFS outward simulatanouely
            while queue:
                temp_len = len(queue)
                temp_val = []
                for _ in range(temp_len):
                    row, col = queue.popleft()
                
                    for dr, dc in DIRECTIONS:
                        new_row, new_col = row+dr, col+dc 
                        if (0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited and result[new_row][new_col] == -1):
                            if grid[new_row][new_col] == 1:
                                return count
                          
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col))
                count += 1
            return -1
        return multi_source_bfs(grid)

                            