class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        memo = {}

        def dp(i, m, n):
            if i == len(strs):
                return 0 
            if (i, m, n) in memo:
                return memo[(i,m,n)]
            
            best = dp(i + 1, m, n)

            
            ones_count = strs[i].count("1")
            zeros_count = strs[i].count("0")
            if ones_count <= n and zeros_count <= m:

                best = max(1+dp(i+1, m-zeros_count, n-ones_count), best)
            memo[(i, m, n)] = best 
            return best 
        return dp(0, m, n)

        