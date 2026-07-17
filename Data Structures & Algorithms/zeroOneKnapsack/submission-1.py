class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        memo = {}
        # Reverse dp :D
        def dp(curr_capacity,idx):
            if idx < 0:
                return 0
            if curr_capacity < weight[idx]:
                return dp(curr_capacity, idx-1)

            if (curr_capacity, idx) in memo:
                return memo[(curr_capacity,idx)]
            
            best = max(profit[idx] + dp(curr_capacity-weight[idx], idx-1), dp(curr_capacity, idx-1))
            memo[(curr_capacity,idx)] = best 
            return best 
        
        return dp(capacity, len(profit)-1)
            

            

           
