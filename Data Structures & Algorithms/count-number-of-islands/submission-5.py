from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(start, visited, grid):
            queue = deque([start])
            visited.add(start)
            ROWS = len(grid)
            COLS = len(grid[0])
            DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

            while queue:
                row, col = queue.popleft()

                for dr, dc in DIRECTIONS:
                    new_row, new_col = row + dr, col+dc 
                    if (0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited and grid[new_row][new_col] == "1"):
                        visited.add((new_row,new_col))
                        queue.append((new_row,new_col))
            
        
        visited = set()
        total = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1"  and (row, col) not in visited:
                    bfs((row,col), visited, grid)
                    total += 1
        return total
        