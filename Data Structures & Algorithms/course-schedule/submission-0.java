

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        return kahns(numCourses, prerequisites);
    }

    // Use Kahn's algorithm for topological sorting.
    public boolean kahns(int n, int[][] prerequisites) {
        Map<Integer, ArrayList<Integer>> graph = new HashMap<>();
        int[] indegree = new int[n];

        // Java's equivalent of Python defaultdict(list)
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }

        for (int[] edge : prerequisites) {
            int course = edge[0];
            int prerequisite = edge[1];

            // prerequisite -> course
            graph.get(prerequisite).add(course);
            indegree[course]++;
        }

        Deque<Integer> queue = new ArrayDeque<>();

        // Start with courses having no prerequisites.
        for (int course = 0; course < n; course++) {
            if (indegree[course] == 0) {
                queue.offer(course);
            }
        }

        int coursesCompleted = 0;

        while (!queue.isEmpty()) {
            int course = queue.poll();
            coursesCompleted++;

            for (int neighbor : graph.get(course)) {
                indegree[neighbor]--;

                if (indegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }

        // All courses can be completed only if every node was processed.
        return coursesCompleted == n;
    }
}