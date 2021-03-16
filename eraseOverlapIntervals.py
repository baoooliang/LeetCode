class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int: 
        if len(intervals) <= 1:
            return 0
        intervals = sorted(intervals)
        lastEnd = intervals[0][1]
        counter = 1
        for interval in intervals[1:]:
            start, end = interval
            if start < lastEnd:
                lastEnd = min(lastEnd, end)
            else:
                counter += 1
                lastEnd = end
        
        return len(intervals) - counter