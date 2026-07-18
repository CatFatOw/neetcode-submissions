import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = list()

        for num in nums:
            heapq.heappush(min_heap, num)

            while len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
        