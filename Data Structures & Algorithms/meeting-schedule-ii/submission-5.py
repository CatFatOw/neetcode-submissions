"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        total = 0
        i = 0
        heap = []
        intervals = sorted(intervals, key=lambda x: x.start)

        while i < len(intervals):
            start = intervals[i].start
            end = intervals[i].end
            i+=1

            if heap:
                if heap[0] > start:
                    total += 1
                else:
                    # We can free it up!
                    heapq.heappop(heap)
                
                heapq.heappush(heap, end)
            else:
                total += 1
                heapq.heappush(heap, end)
        return total
        
        