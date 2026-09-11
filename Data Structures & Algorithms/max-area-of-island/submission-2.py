from collections import deque 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        grid[i] = 0 (water)
        grid[i]  = 1 (land)

        area = # cells in the islands


        APPORACH: use bfs each time we find an islalnd we record the number ofcells etc
        """

        def bfs(start, visited, grid):
            area = 1
            ROWS = len(grid)
            COLS = len(grid[0])
            DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
            queue = deque([start])
            visited.add(start)

            while queue:
                row, col = queue.popleft()
                
                
                for dr, dc in DIRECTIONS:
                    new_row, new_col = row + dr, col + dc 
                    if (0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited):
                        area += 1
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
            return area 
        
        max_area = 0
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if ((row,col) not in visited and grid[row][col] == 1):
                    area = bfs((row,col), visited, grid)
                    max_area = max(max_area, area)
        return max_area
                
                

        