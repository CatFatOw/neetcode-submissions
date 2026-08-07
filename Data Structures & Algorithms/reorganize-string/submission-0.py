import heapq
from collections import defaultdict
class Solution:
    def reorganizeString(self, s: str) -> str:
        mapping = defaultdict(int)

        for char in s:
            mapping[char] += 1
        
        heap = []
        just_used = []

        # populate the heap 
        for char, freq in mapping.items():
            heapq.heappush(heap, (-freq, char))
        
        out = ""
        while heap:
            freq, num = heapq.heappop(heap)
            out+=num 
            freq += 1

            if just_used:
                p_freq, p_num = heapq.heappop(just_used)
                
                heapq.heappush(heap, (p_freq, p_num))

            if freq < 0:
                heapq.heappush(just_used, (freq, num))
               

        if just_used:
            return ""
        return out
            
            


        