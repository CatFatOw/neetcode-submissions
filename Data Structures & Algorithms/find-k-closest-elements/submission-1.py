import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # max_heap
        heap = []

        for i in range(len(arr)):
            distance = abs(arr[i] - x)
            heapq.heappush(heap, (-distance, -arr[i]))

            # When it exceeds k we start poppings
            while len(heap) > k:
                heapq.heappop(heap)
        
        # the heap results should be [(-dista, a)]
        return sorted([-y for x,y in heap])
        