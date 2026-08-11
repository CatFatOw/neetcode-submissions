from collections import deque 
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        def bfs():
            queue = deque([["0", "0", "0","0"]])
            visited = set(["0000"])
            operations = 0

            while queue:
                temp_len = len(queue)
                for _ in range(temp_len):
                    combination = queue.popleft()

                    if combination == list(target):
                        return operations
                
                    for i in range(4):
                        for number in [-1, 1]:
                            new_combination = list(combination)
                            new_combination[i]  = str((int(new_combination[i]) + number) % 10)
                          

                            str_new_combination = "".join(new_combination)
                            if str_new_combination not in visited and str_new_combination not in deadends:
                                queue.append(new_combination)
                                visited.add(str_new_combination)
                operations += 1
                
            return -1
        return bfs()

            