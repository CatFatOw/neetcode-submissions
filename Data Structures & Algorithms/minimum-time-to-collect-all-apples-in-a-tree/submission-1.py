from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        n vertices from 0 to n-1
        some apples in the vertices 
        every edge takes 1 second to walk

        return the min time to collect all apples in the tree, starting at vertex 0 and then coming back 

        edges[i] = a[i] <-> b[i]
        and boolean with hasApplu[i] = true
        """
        mapping = defaultdict(list)

        for u, v in edges:
            mapping[u].append(v)
            mapping[v].append(u)
        
        def dfs(root, visited):
            time = 0
            for neighbor in mapping[root]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_time = dfs(neighbor, visited)

                    if new_time > 0 or hasApple[neighbor]:
                        time += new_time + 2
            return time 
        return dfs(0, {0})
            
        