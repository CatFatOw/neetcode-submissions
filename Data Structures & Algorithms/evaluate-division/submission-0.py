from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        equations: [a, b] | equations[i] = [A, B]
        values:  arr of real numbers where values[i]= Ai / Bi
        A and B represents a string of a single variable 

        queries: arr where queries[j] = [C, D]
        represents such that you have to find the answer of Cj / Dj ???

        Ok, we treat this as a undirected graph with edges as weights. then, through each query we multiply the values and once we hit the final value wereturn the value otherwise we return -1 :D 


        """

        def get_mapping(equations, values):
            mapping = defaultdict(list)
            index = 0
            for u,v in equations:
                weight = values[index]
                mapping[u].append((v, weight))
                mapping[v].append((u, 1 / weight))
                index += 1
            
            return mapping 
        mapping = get_mapping(equations, values)

        def dfs(start, stop, visited, total):


            if start == stop:
                return total 
            
            for neighbor, weight in mapping[start]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    result = dfs(neighbor, stop, visited, total*weight)
                    if result != -1:
                        return result

           
            return -1
                
            

        ans = []
        for start, stop in queries:
            if start not in mapping or stop not in mapping:
                ans.append(-1)
            else:
                total = 1
                visited = set()
                result = dfs(start, stop, visited, total)
                ans.append(result)
        return ans


        



       
            