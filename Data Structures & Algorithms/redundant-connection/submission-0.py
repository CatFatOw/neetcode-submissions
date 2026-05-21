class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = {}

        for i in range(1, len(edges)+1):
            parents[i] = i 
        
        def find(x):
            if parents[x] != x:
                return find(parents[x])
            else:
                return x

        def union(x, y):
            parents[find(y)] = find(x)


        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            else:
                union(u, v)
        
        