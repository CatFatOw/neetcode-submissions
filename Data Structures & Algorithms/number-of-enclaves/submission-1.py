from collections import deque 
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        def bfs(start, visited):
            queue = deque([start])
            visited.add(start)
            DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
            ROWS = len(grid)
            COLS = len(grid[0])
            count = 0
            notvalid=False

            while queue:
                temp_len = len(queue)
                for _ in range(temp_len):
                    row, col = queue.popleft()
                    if row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1:
                        notvalid=True

                    count += 1
                    for dr, dc in DIRECTIONS:
                        new_row, new_col = row+dr, col+dc 

                        if ((0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row,new_col) not in visited) and grid[new_row][new_col] == 1):
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col))
            return count if not notvalid else 0 
        
        total = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col] == 1:
                    total += bfs((row,col), visited)
                    
        return total



            
        