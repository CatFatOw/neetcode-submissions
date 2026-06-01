from collections import defaultdict
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        temp = []

        def backtrack(open_count, closed_count):
            # Base case
            if open_count + closed_count == n * 2:
                result.append("".join(temp))
                return 
            
            if closed_count < open_count:
                temp.append(")")
                backtrack(open_count, closed_count+1)
                temp.pop(-1)
            
            if open_count < n:
                temp.append("(")
                backtrack(open_count+1, closed_count)
                temp.pop(-1)
        backtrack(0, 0)
        return result
            
            


        