from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def convert_adj_list(isConnected):
            adj_list = defaultdict(list)
            for row in range(len(isConnected)):
                for col in range(len(isConnected[0])):
                    val = isConnected[row][col] 
                    if val == 1 and row!= col:
                        adj_list[row].append(col)
            return adj_list 
        adj_list = convert_adj_list(isConnected)

        n_provinces = 0
        visited = set()

        def dfs(node, adj_list, visited):
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, adj_list, visited)

        for node in range(len(isConnected)):
            if node not in visited:
                dfs(node, adj_list, visited)
                n_provinces += 1
        return n_provinces
        
        

        