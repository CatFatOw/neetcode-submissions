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
        """
        [start_1, end_1], etc.

        find minimum # of rooms required to schedule all meetings without conflicts 

        make the min heap only store the end values 

        1. sort by increasing start value 
        [(0,40), (5,10), (15,20)]
        heappush each new element into a min heap

        2. if heap then compare the min value with the current value. 
        if the end >= start then add total by 1 
        then heappush


        """
        intervals = sorted(intervals, key=lambda x: x.start)
        total = 0
        heap = []
        i = 0

        while i < len(intervals):
            start = intervals[i].start
            end = intervals[i].end
            i+=1

            if heap:
            
                if heap[0] > start:
                    
                    total += 1
                else:
                    heapq.heappop(heap)
                heapq.heappush(heap, end)
                    

            else:
                total += 1
                heapq.heappush(heap, end)
        return total

        