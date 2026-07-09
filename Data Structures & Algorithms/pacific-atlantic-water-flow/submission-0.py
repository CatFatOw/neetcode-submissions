from collections import deque 
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def bfs(row, col, visited):
            queue = deque([(row, col)])
            visited.add((row, col))
            DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
            ROWS = len(heights)
            COLS = len(heights[0])

            while queue:
                row, col = queue.popleft()
                for dr, dc in DIRECTIONS:
                    new_row, new_col = row + dr, col+dc
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited and heights[new_row][new_col] >= heights[row][col]:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
        
        # Populate the sides 
        p_set = set()
        a_set = set()
        for row in range(len(heights)):
            if (row, 0) not in p_set:
                bfs(row, 0, p_set)
            if (row, len(heights[0])-1) not in a_set:
                bfs(row, len(heights[0])-1, a_set)
        
        for col in range(len(heights[0])):
            if (0, col) not in p_set:
                bfs(0, col, p_set)
            if (len(heights)-1, col) not in a_set:
                bfs(len(heights)-1, col, a_set)
        result = [list(cell) for cell in a_set.intersection(p_set)]
        return result

        