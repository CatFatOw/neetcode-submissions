import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []
        for x, y in points:
            d_2 = (x**2) + (y**2)
            heapq.heappush(max_heap, (-d_2, [x,y]))

            while len(max_heap) > k:
                heapq.heappop(max_heap)

        return [x for _, x in max_heap]

        