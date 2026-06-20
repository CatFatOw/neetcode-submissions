import math 
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check_valid(curr_weight, weights, days):
            total_sum = sum(weights)

            weight_total = 0
            i = 0
            for _ in range(days):
                total = 0
                while i < len(weights) and total + weights[i] <= curr_weight:
                    total += weights[i]
                    i += 1
                
                weight_total += total

            return weight_total == total_sum

        ans = float("inf")
        left = max(weights)
        right = sum(weights)
        while left <= right:
            curr_weight = (left + right) // 2
            if check_valid(curr_weight, weights, days):
                ans = min(ans, curr_weight)
                right = curr_weight - 1
            else:
                left = curr_weight + 1
        return ans


                



            

        