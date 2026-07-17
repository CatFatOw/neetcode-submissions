import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
        # max heap's largest value 
        else:
            val = self.max_heap[0]
            if num > -val:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        
        # Max heap should always be == or greater than 1
        if len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        elif len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return ((self.min_heap[0] + -self.max_heap[0] )/2 )
        elif self.max_heap:
            return -self.max_heap[0]
        return self.min_heap[0]


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()