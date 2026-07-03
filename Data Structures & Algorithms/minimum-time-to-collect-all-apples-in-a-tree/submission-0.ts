class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @param {boolean[]} hasApple
     * @return {number}
     */
    minTime(n: number, edges: number[][], hasApple: boolean[]): number {
        function getList(map: Map<number, number[]>, key: number): number[] {
    if (!map.has(key)) {
        map.set(key, []);
    }
    return map.get(key)!;
}
    
    function get_adj_list(edges:number[][]){
        const graph = new Map<number, number[]>();
        for (const [u,v] of edges){
            getList(graph, u).push(v);
            getList(graph, v).push(u);
        }
        return graph;
    }
    let adj_list = get_adj_list(edges);
    let visited = new Set<number>();
    function dfs(root:number, adj_list:Map<number, number[]>, visited:Set<number>){
        visited.add(root);
        
        let time:number = 0;
        for (const neighbor of adj_list.get(root)??[]){
            if (!visited.has(neighbor)){
                let child_time = dfs(neighbor, adj_list, visited);

                if (hasApple[neighbor] || child_time > 0){
                    time += child_time + 2;
                }
            }
        }
        return time;


    }
    return dfs(0, adj_list, visited);
    }

    
}
