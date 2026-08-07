from typing import List
from collections import deque, defaultdict

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        def get_target_candies(board):
            # scan for all rows
            removed_rows = set()
            to_remove = set()
            # Sliding window style :D

            for row in range(len(board)):
                count = 1
                target_num = board[row][0]
                positions = [(row,0)]

                for col in range(1, len(board[row])):
                    if board[row][col] == target_num:
                        positions.append((row,col))
                        count += 1

                    elif target_num != 0 and count >= 3:
                        for ROW, COL in positions:
                            removed_rows.add(ROW)
                            to_remove.add((ROW,COL))
                        target_num = board[row][col]
                        positions = [(row,col)]
                        count = 1

                    else:
                        target_num = board[row][col]
                        positions = [(row,col)]
                        count = 1
                if count >= 3 and target_num != 0:
                    for ROW, COL in positions:
                        removed_rows.add(ROW)
                        to_remove.add((ROW,COL))

            # scan columns
            for col in range(len(board[0])):
                count = 1
                target_num = board[0][col]
                positions = [(0, col)]

                for row in range(1, len(board)):
                    if board[row][col] == target_num:
                        positions.append((row,col))
                        count += 1

                    elif count >= 3 and target_num != 0:
                        for ROW, COL in positions:
                            removed_rows.add(ROW)
                            to_remove.add((ROW,COL))
                        target_num = board[row][col]
                        positions = [(row,col)]
                        count = 1

                    else:
                        target_num = board[row][col]
                        positions = [(row,col)]
                        count = 1
                if count >= 3 and target_num != 0:
                    for ROW, COL in positions:
                        removed_rows.add(ROW)
                        to_remove.add((ROW,COL))
            for row, col in to_remove:
                board[row][col] = 0
            return board, removed_rows

        def apply_gravity(board):
            rows = len(board)
            cols = len(board[0])

            for col in range(cols):
                write_row = rows - 1

                for row in range(rows - 1, -1, -1):
                    if board[row][col] != 0:
                        board[write_row][col] = board[row][col]
                        write_row -= 1

                for row in range(write_row, -1, -1):
                    board[row][col] = 0

            return board

        board, removed_rows = get_target_candies(board)
        while removed_rows:

            board = apply_gravity(board)
            board, removed_rows = get_target_candies(board)

            #print(board, removed_rows)
        return board