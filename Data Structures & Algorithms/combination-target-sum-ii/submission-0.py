class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        temp = []
        visited = set()

        def backtrack(i):
            # Base case 
            if sum(temp) > target:
                return
            
            if sum(temp) == target:
                result.append(temp.copy())
                return 
            
            
            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx-1]:
                    continue
                # backtrack 
                temp.append(candidates[idx])
                
                backtrack(idx+1)
                # go back
                temp.pop(-1)
        backtrack(0)
        return result
        
        