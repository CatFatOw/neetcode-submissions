class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        temp = []

        def backtrack(start):
            if len(temp) == k:
                result.append(temp.copy())
                return
            

            for j in range(start, n+1):
                temp.append(j)
                backtrack(j+1)
                temp.pop()
        backtrack(1)
        return result
            