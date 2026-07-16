from collections import deque, defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        def make_adj_list(edges):
            mapping = defaultdict(list)
            for u, v in edges:
                mapping[u].append(v)
                mapping[v].append(u)
            return mapping 

        adj_list = make_adj_list(edges)


        def isConnected(n, adj_list):
            queue = deque([0])
            visited = set([0])

            while queue:
                node = queue.popleft()

                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            if len(visited) == n:
                return True 
            return False 

        # Determine edges = n-1
        if len(edges) != n-1:
            return False 
        # Determine if tree is connected 
        # If tree is disconnected that automatically rules out cycles
        if not isConnected(n, adj_list):
            return False 
        return True
        
        
