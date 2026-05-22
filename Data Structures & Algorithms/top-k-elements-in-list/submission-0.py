from collections import defaultdict 
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int)
        for num in nums:
            mapping[num] += 1
        
        min_heap = []
        for val, freq in mapping.items():
            heapq.heappush(min_heap, (freq, val))

            while len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # We are left with the top k more frequent elements 
        result = []
        for freq, val in min_heap:
            result.append(val)
        return result
        