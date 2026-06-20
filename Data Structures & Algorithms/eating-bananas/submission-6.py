import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(k, piles, h):
            hours = sum(math.ceil(pile / k) for pile in piles)
            return hours <= h


        left = 1
        right = max(piles)
        ans = float("inf")
        while left <= right:
            k = math.ceil((left + right) / 2)
            if can_eat(k, piles, h):
                ans = min(ans, k)
                right = k-1
            else:
                left = k + 1
        return ans
        