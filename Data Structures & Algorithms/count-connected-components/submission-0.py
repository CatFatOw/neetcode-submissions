from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        visited = set()

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node, adj_list, visited):
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, adj_list, visited)
        
        components = 0
        for node in range(n):
            if node not in visited:
                dfs(node, adj_list, visited)
                components += 1
        return components

        