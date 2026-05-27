import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def valid(k, piles, h):
            hours = 0
            for pile in piles:
                if pile <= k:
                    hours += 1
                else:
                    hours += math.ceil((pile/k))
            
            if hours <= h:
                return True 
            else:
                return False 

         # create the solution space 
        left = 1
        right = max(piles)-1
        min_ans = max(piles)

        while left <= right:
            mid = (left + right) // 2
            k_candidate = mid
            if valid(k_candidate, piles, h):
                min_ans = min(k_candidate, min_ans)
                right = mid - 1
            else:
                left = mid + 1
        return min_ans

        


            
        
