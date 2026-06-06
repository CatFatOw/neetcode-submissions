import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int)
        for num in nums:
            mapping[num] += 1
        heap = []
        for num, freq in mapping.items():
            heapq.heappush(heap, (freq, num))
            while len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]
        