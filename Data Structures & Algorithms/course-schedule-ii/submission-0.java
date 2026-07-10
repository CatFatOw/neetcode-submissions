class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        return khan(numCourses, prerequisites);
        
    }

    public int[] khan(int n, int[][] prerequisites){
        HashMap<Integer, ArrayList<Integer>> adj_list  = new HashMap<>();
        int[] indegree = new int[n];

        for (int i = 0; i < n; i++) {
            adj_list.put(i, new ArrayList<>());
        }

        //populate the hashmap
        for (int cell[] : prerequisites){
            int course = cell[0];
            int prereq = cell[1];
            adj_list.get(prereq).add(course);
            indegree[course] ++;
        }

        Deque<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++){
            if (indegree[i] == 0){
                queue.offer(i);
            
            }
        }
        ArrayList<Integer> order = new ArrayList<>();

        while (!queue.isEmpty()){
            int node = queue.pollFirst();
            order.add(node);

            for (int neighbor : adj_list.get(node)){
                indegree[neighbor] -= 1;
                if (indegree[neighbor] == 0){
                    queue.offer(neighbor);
                }
            }
        }
        if (order.size() != n){
            return new int[0];
        }
        int[] result = new int[order.size()];

        for (int i = 0; i < order.size(); i++) {
            result[i] = order.get(i);
        }

        return result;
    }
}