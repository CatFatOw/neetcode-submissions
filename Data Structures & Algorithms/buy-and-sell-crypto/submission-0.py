class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, state, transaction_limit):
            if i >= len(prices) or transaction_limit == 0:
                return 0
            if (i, state, transaction_limit) in memo:
                return memo[(i,state, transaction_limit)]
            
            # if state = 0 we sell the stock
            if state == 0:
                best = max(prices[i] + dp(i+1, 1, transaction_limit-1), dp(i+1,0, transaction_limit))
            else:
                best = max(-prices[i] + dp(i+1, 0, transaction_limit), dp(i+1, 1, transaction_limit))
            memo[(i,state, transaction_limit)] = best
            return best
        return dp(0, 1, 1)
        