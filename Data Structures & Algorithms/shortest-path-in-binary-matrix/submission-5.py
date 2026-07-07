from collections import deque 
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def bfs(start, visited, grid):
            queue = deque([start])
            visited.add(start)
            ROWS = len(grid)
            COLS = len(grid[0])
            count = 0
            DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1, -1)]

            if grid[0][0] == 1:
                return -1
            if grid[-1][-1] == 1:
                return -1
            
            while queue:
                count += 1
                temp_len = len(queue)
                for _ in range(temp_len):
                    row, col = queue.popleft()

                    if row == len(grid)-1 and col == len(grid)-1:
                        return count

                    for dr, dc in DIRECTIONS:
                        new_row, new_col = row + dr, col + dc 
                        if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited and grid[new_row][new_col] == 0:
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col))
            return -1  

        return bfs((0,0), set(), grid)


        