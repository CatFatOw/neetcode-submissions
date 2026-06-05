class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        memo = {}
        def dp(n, k):
            if n == k or k == 0:
                return 1
            if (n,k) in memo:
                return memo[(n,k)]
            
            best = dp(n-1, k) + dp(n-1, k-1)
            memo[(n,k)] = best 
            return best 
        
        result = []
        for k in range(rowIndex+1):
            result.append(dp(rowIndex, k))
        return result
        