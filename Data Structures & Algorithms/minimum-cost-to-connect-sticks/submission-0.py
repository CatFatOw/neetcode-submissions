import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_heap = list(sticks)
        heapq.heapify(min_heap)
        min_cost = 0

        while len(min_heap) > 1:
            stick1 = heapq.heappop(min_heap)
            stick2 = heapq.heappop(min_heap)
            min_cost += stick1 + stick2 
            heapq.heappush(min_heap, stick1+stick2)
        return min_cost
 

        