import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEat(mid):
            total_time = 0

            for pile in piles:
                total_time += math.ceil(pile/mid)
            return total_time <= h
            
        
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            if canEat(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
        