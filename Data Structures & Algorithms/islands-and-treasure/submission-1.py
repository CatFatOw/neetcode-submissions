from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        INF: land that can be traversed 
        0 a treasure chest 
        -1 water 9can't be traversed)

        we start at 0 (the treasure chest) and then use multi-source BFS to inf
        """
        DIRECTIONS = [(1,0), (-1,0), (0,-1), (0,1)]
        queue = deque()
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))
        while queue:
            row, col, length = queue.popleft()

            for dr, dc in DIRECTIONS:
                new_row, new_col = row + dr, col + dc 
                if 0 <= new_row and new_row < ROWS and 0 <= new_col and new_col < COLS:

                    new_node = (new_row, new_col)
                    if new_node not in visited and grid[new_row][new_col] == 2147483647:
                        queue.append((new_row, new_col, length + 1))
                        visited.add(new_node)
                        # neighbor distance = curr_disatnce + 1
                        grid[new_row][new_col] = grid[row][col] + 1