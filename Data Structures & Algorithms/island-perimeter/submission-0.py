from collections import deque 
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def matrix_bfs(row, col, grid, length):
            ROWS = len(grid)
            COLS = len(grid[0])
            queue = deque([(row, col)])
            visited = set([(row, col)])

            DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

            while queue:
                row, col = queue.popleft()
                for dr, dc in DIRECTIONS:
                    new_row = row + dr
                    new_col = col + dc 

            
                    if (new_row < 0 or new_row >= ROWS) or (new_col < 0 or new_col >= COLS):
                        length += 1

                    elif 0 <= new_row < ROWS and 0 <= new_col < COLS:
                        if (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col))
                        elif (new_row, new_col) not in visited:
                            length += 1
            return length

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return matrix_bfs(row, col, grid, 0)

        