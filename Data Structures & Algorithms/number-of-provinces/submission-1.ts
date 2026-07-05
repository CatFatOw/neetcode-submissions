class Solution {
    /**
     * @param {number[][]} isConnected
     * @return {number}
     */
    findCircleNum(isConnected: number[][]): number {
        function bfs(start: number, visited: Set<number>, grid: number[][]): void {
            const queue: number[] = [start];
            visited.add(start);

            while (queue.length > 0) {
                const node = queue.shift()!;

                for (let neighbor = 0; neighbor < grid.length; neighbor++) {
                    if (!visited.has(neighbor) && grid[node][neighbor] === 1) {
                        visited.add(neighbor);
                        queue.push(neighbor);
                    }
                }
            }
        }

        let provinces = 0;
        const visited = new Set<number>();

        for (let i = 0; i < isConnected.length; i++) {
            if (!visited.has(i)) {
                bfs(i, visited, isConnected);
                provinces++;
            }
        }

        return provinces;
    }
}