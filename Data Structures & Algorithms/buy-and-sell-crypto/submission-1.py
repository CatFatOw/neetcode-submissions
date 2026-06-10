class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        left = 0
        for right in range(len(prices)):
            while prices[left] > prices[right] and left != right:
                left = right 
            profit = max(profit, prices[right]-prices[left])
        return profit

        