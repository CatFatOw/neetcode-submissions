import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1 * x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            num1 = heapq.heappop(max_heap)
            num2 = heapq.heappop(max_heap)

            if num1 == num2:
                pass 
            elif num1 < num2:
                heapq.heappush(max_heap, -1 * (num2-num1))
        
        if max_heap:
            return -1 * max_heap[0]
        return 0
        