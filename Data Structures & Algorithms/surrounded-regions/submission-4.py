from collections import defaultdict, deque 
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_edge(row, col):
            return row == 0 or row == len(board)-1 or col == 0 or col == len(board[0])-1


        def bfs(start, visited):
            queue = deque([start])
            visited.add(start)
            DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
            ROWS = len(board)
            COLS = len(board[0])
            result = []

            while queue:
                row, col = queue.popleft()
                result.append((row,col))
                
                for dr, dc in DIRECTIONS:
                    new_row, new_col = row + dr, col + dc 
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited and board[new_row][new_col] == "O":
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
            return result
        visited = set()
        result = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row,col) not in visited and board[row][col] == "O":
                    result.append(bfs((row,col), visited))
        
        change = []
        for island in result:
            temp = []
            if island:
                for row, col in island:
                    temp.append((row,col))
                    if is_edge(row,col):
                        temp = []
                        break
                change.extend(temp)
            for row, col in change:
                board[row][col] = "X"

                        

            