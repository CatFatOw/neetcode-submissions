from collections import deque 
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        def can_reach(start, k):
            queue = deque([start])
            seen = set([start])
            ROWS = len(heights)
            COLS = len(heights[0])
            DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

            while queue:
                row, col = queue.popleft()

                if row == len(heights) - 1 and col == len(heights[0]) - 1:
                    return True 

                for dr, dc in DIRECTIONS:
                    new_row, new_col = row + dr, col + dc 

                    if 0 <= new_row and new_row < ROWS and 0 <= new_col and new_col < COLS and abs(heights[new_row][new_col] - heights[row][col]) <= k:
                        if (new_row, new_col) not in seen:
                            seen.add((new_row, new_col))
                            queue.append((new_row, new_col))
            return False


        # Binary search
        left = 0
        max_height = max(max(row) for row in heights)
        min_height = min(min(row) for row in heights)
        right = max_height - min_height 

        ans = right
        while left <= right:
            mid = (left + right) // 2
            if can_reach((0,0), mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans

            

        