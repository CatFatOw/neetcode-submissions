from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def grid_bfs(start_node, grid):
            queue = deque([(start_node[0], start_node[1], 1)])
            visited = set([start_node])
            DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1, 1), (-1, -1)]
            ROWS = len(grid)
            COLS = len(grid[0])


            while queue:
                row, col, length = queue.popleft()

                if row == ROWS-1 and col == COLS - 1:
                    return length
    

                for dr, dc in DIRECTIONS:
                    new_row = row + dr 
                    new_col = col + dc 

                    if 0 <= new_row and new_row < ROWS and 0 <= new_col and new_col < COLS:
                        new_node = (new_row, new_col)
                        if new_node not in visited and grid[new_row][new_col] == 0:
                            queue.append((new_row, new_col, length+1))
                            visited.add(new_node)
    
            return -1

        if grid[0][0] == 1:
            return -1
        else:
            result = grid_bfs((0,0), grid)
            return result

        
        