class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(i):
            if i == 0:
                return 0
            if i < 0:
                return -1

            if i in memo:
                return memo[i]
            
            best = float("inf")
            for coin in coins:
                if dp(i-coin) != -1:
                    best = min(best, 1 + dp(i - coin))
            if best != -1:
                memo[i] = best 
            return best 

        result = dp(amount)
        if result == float("inf"):
            return -1
        return result


        