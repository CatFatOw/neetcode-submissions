class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        total_apples = 0
        total_weight = 5000

        for apple_weight in weight:
            if apple_weight <= total_weight:
                total_apples += 1
                total_weight -= apple_weight
        return total_apples

        