import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        for num in arr:
            heapq.heappush(max_heap, (-1*abs(x-num), -num))

            while len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return sorted([-y for x, y in max_heap])

        