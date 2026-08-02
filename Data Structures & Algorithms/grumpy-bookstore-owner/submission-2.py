class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # create a baseline 
        baseline = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                baseline += customers[i]
            
        
        # Create a sliding window to find the best possible useage? 
        max_extra = 0
        curr_extra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                curr_extra += customers[i]

        max_extra = max(max_extra, curr_extra)

        for i in range(minutes, len(customers)):
            if grumpy[i-minutes] == 1:
                curr_extra -= customers[i-minutes]
            if grumpy[i] == 1:
                curr_extra += customers[i]
            max_extra = max(max_extra, curr_extra)

        return max_extra + baseline
        