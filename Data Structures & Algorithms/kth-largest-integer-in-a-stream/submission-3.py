import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(nums)
        self.heap = nums
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
