class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals 

        intervals = sorted(intervals, key=lambda x: x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if result[-1][-1] < intervals[i][0]:
                result.append(intervals[i])
            elif result[-1][-1] >= intervals[i][0] and result[-1][-1] <= intervals[i][-1]:
                result[-1][-1] = intervals[i][-1]
        
        return result

        

        