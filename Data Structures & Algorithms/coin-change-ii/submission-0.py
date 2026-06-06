class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i, amount):
            if i >= len(coins) or amount < 0:
                return 0
            if amount == 0:
                return 1
            
            if (i, amount) in memo:
                return memo[(i, amount)]
            
            total = dp(i, amount-coins[i]) + dp(i+1, amount)
            memo[(i, amount)] = total
            return total
        return dp(0, amount)

        