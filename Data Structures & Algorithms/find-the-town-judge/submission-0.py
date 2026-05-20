from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1
        in_degree_map = defaultdict(list)
        out_degree_map = defaultdict(list)
        unique_node = set()

        
        for u, v in trust:
            if u not in unique_node:
                unique_node.add(u)
            if v not in unique_node:
                unique_node.add(v)

            in_degree_map[v].append(u)
            out_degree_map[u].append(u)
        

        # Find the unique arr
        judge = set()
        for node, in_nodes in in_degree_map.items():
            if len(in_nodes) == len(unique_node) - 1 and  len(out_degree_map[node]) == 0:
                judge.add(node)
    
        if len(judge) == 1:
            return list(judge)[0]
        return -1
        