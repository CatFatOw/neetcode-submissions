class Solution {
    public int shortestBridge(int[][] grid) {
        /**Core logic:
        BFS to find 1 island
        Use multi-source BFS for each island cell and return the count :D  */

        boolean isFound = false;
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        for (int row = 0; row < grid.length; row++){
            for (int col = 0; col < grid[0].length; col++){
                if (!visited[row][col] && grid[row][col] == 1){
                    ArrayList<int[]> islands = bfs(row, col,visited, grid);
                    isFound = true;
                    break;
                }
            }
            if (isFound){
                break;
            }

        }

        // RUN multi-source BFS on the islands
        return multi_bfs(grid, visited);
        
    }

    public ArrayList<int[]> bfs(int row, int col, boolean[][] visited, int[][] grid){
        Deque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] {row, col});
        visited[row][col] = true;
        int[][] DIRECTIONS = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        int ROWS = grid.length;
        int COLS = grid[0].length;
        ArrayList<int[]> islands = new ArrayList<>();

        while (!queue.isEmpty()){
            int[] c1 = queue.pollFirst();
            int r = c1[0];
            int c = c1[1];
            islands.add(new int[] {r, c});

            for (int[] cell : DIRECTIONS){
                int new_row = r + cell[0];
                int new_col = c + cell[1];

                if (0 <= new_row && new_row < ROWS && 0 <= new_col && new_col < COLS && !visited[new_row][new_col] && grid[new_row][new_col] == 1){
                    visited[new_row][new_col] = true;
                    queue.offer(new int[] {new_row, new_col});
                }
            }

        }
        return islands;
    }


    public int multi_bfs(int[][] grid, boolean[][] visited){
        int ROWS = grid.length;
        int COLS = grid[0].length;
        int[][] DIRECTIONS = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        Deque<int[]> queue = new ArrayDeque<>();
        int count = 0;

        // //results 
        // //defaults to 0 so we must fill
        // int[] result = new int [ROWS][COLS];

        // for (int i = 0; i < ROWS; i++){
        //     Arrays.fill(result[i], -1);
        // }

        //put all islands cells into the queue and mark them as visited :D 
        for (int row = 0; row < ROWS; row ++ ){
            for (int col = 0; col < COLS; col ++){
                if (visited[row][col]){
                    queue.offer(new int[] {row, col});
                }

            }
        }

        while (!queue.isEmpty()){
            int temp_len = queue.size();
            for (int i = 0; i < temp_len;i++){
                int[] cell = queue.pollFirst();
            int row = cell[0];
            int col = cell[1];

            for (int[] neighbor : DIRECTIONS){
                int new_row = row + neighbor[0];
                int new_col = col + neighbor[1];

                if (0 <= new_row && new_row < ROWS && 0 <= new_col && new_col < COLS && !visited[new_row][new_col]){
                    if (grid[new_row][new_col] == 1){
                        return count;
                    }
                    queue.offer(new int[] {new_row, new_col});
                    visited[new_row][new_col] = true;
                
                }
            }
            

            }
            count++;
            
            
        }
        return count;
        
}
    }
