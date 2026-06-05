class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        memo = {}
        

        def dp(n, k):
            if n == k or k == 0:
                return 1
            
            if (n, k) in memo:
                return memo[(n,k)]
            
            best = dp(n-1, k) + dp(n-1, k-1)
            memo[(n,k)] = best 
            return best 
        
        result = []
        for n in range(numRows):
            arr = []
            for k in range(n+1): 
                arr.append(dp(n, k))
            result.append(arr)
        return result

                
            