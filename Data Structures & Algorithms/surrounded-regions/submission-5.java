class Solution {
    public void solve(char[][] board) {
        if (board == null || board.length == 0) {
            return;
        }

        boolean[][] visited = new boolean[board.length][board[0].length];
        List<List<int[]>> regions = new ArrayList<>();

        for (int row = 0; row < board.length; row++) {
            for (int col = 0; col < board[0].length; col++) {
                if (!visited[row][col] && board[row][col] == 'O') {
                    List<int[]> region = bfs(
                        new int[] {row, col},
                        board,
                        visited
                    );

                    regions.add(region);
                }
            }
        }

        for (List<int[]> region : regions) {
            boolean touchesEdge = false;

            for (int[] cell : region) {
                int row = cell[0];
                int col = cell[1];

                if (isEdge(row, col, board)) {
                    touchesEdge = true;
                    break;
                }
            }

            if (!touchesEdge) {
                for (int[] cell : region) {
                    board[cell[0]][cell[1]] = 'X';
                }
            }
        }
    }

    public List<int[]> bfs(
        int[] start,
        char[][] board,
        boolean[][] visited
    ) {
        Deque<int[]> queue = new ArrayDeque<>();
        List<int[]> region = new ArrayList<>();

        queue.offer(start);
        visited[start[0]][start[1]] = true;

        int[][] directions = {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };

        int rows = board.length;
        int cols = board[0].length;

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int row = cell[0];
            int col = cell[1];

            region.add(new int[] {row, col});

            for (int[] direction : directions) {
                int newRow = row + direction[0];
                int newCol = col + direction[1];

                if (
                    newRow >= 0 &&
                    newRow < rows &&
                    newCol >= 0 &&
                    newCol < cols &&
                    !visited[newRow][newCol] &&
                    board[newRow][newCol] == 'O'
                ) {
                    visited[newRow][newCol] = true;
                    queue.offer(new int[] {newRow, newCol});
                }
            }
        }

        return region;
    }

    public boolean isEdge(int row, int col, char[][] board) {
        return (
            row == 0 ||
            row == board.length - 1 ||
            col == 0 ||
            col == board[0].length - 1
        );
    }
}