import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def koko_eat(rate, piles, h):
            return sum([math.ceil(p/rate) for p in piles]) <= h
        
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2

            if koko_eat(mid, piles,h):
                right = mid -1 
            else:
                left = mid + 1
        return left

        