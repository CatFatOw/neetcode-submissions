class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def dp(i, j):
            if i == len(s):
                return True

            if i > len(s) or j > len(s):
                return False 
            
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if s[i:j] in wordDict:
                result = dp(j, j+1) or dp(i, j+1)
            else:
                result = dp(i,j+1)
            memo[(i,j)] = result
            return result
        return dp(0, 0)
