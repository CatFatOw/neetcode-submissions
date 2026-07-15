class Solution {
    public int islandPerimeter(int[][] grid) {
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {
                if (grid[row][col] == 1) {
                    return bfs(new int[]{row, col}, grid);
                }
            }
        }

        return 0;
    }

    public int bfs(int[] start, int[][] grid) {
        Deque<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[grid.length][grid[0].length];

        int[][] DIRECTIONS = {
            {1, 0}, {0, 1}, {-1, 0}, {0, -1}
        };

        int total = 0;
        int ROWS = grid.length;
        int COLS = grid[0].length;

        queue.offer(start);
        visited[start[0]][start[1]] = true;

        while (!queue.isEmpty()) {
            int[] cell = queue.pollFirst();
            int row = cell[0];
            int col = cell[1];

            for (int[] neighbor : DIRECTIONS) {
                int newRow = row + neighbor[0];
                int newCol = col + neighbor[1];

                // Edge of the grid = perimeter
                if (!(0 <= newRow && newRow < ROWS
                        && 0 <= newCol && newCol < COLS)) {
                    total++;
                }

                // Water next to land = perimeter
                else if (grid[newRow][newCol] == 0) {
                    total++;
                }

                // Unvisited land: continue BFS
                else if (!visited[newRow][newCol]) {
                    visited[newRow][newCol] = true;
                    queue.offer(new int[]{newRow, newCol});
                }
            }
        }

        return total;
    }
}