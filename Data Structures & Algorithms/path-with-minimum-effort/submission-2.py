from collections import deque 
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        def canReach(max_diff):
            queue = deque([(0,0)])
            visited = set([(0,0)])
            ROWS = len(heights)
            COLS = len(heights[0])
            DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]

            while queue:
                row, col = queue.popleft()

                if row == ROWS - 1 and col == COLS - 1:
                    return True

                for dr, dc in DIRECTIONS:
                    new_row, new_col = row+dr, col + dc 
                    if (0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited and abs(heights[new_row][new_col] - heights[row][col]) <= max_diff):
                        visited.add((new_row,new_col))
                        queue.append((new_row,new_col))
            return False


        low = 0
        high = 10**6

        while low <= high:
            mid = (low + high) // 2
            if canReach(mid):
                high = mid-1
            else:
                low = mid + 1
        return low
        