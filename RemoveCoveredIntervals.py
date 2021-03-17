class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: (i[0], -i[1]))
        if len(intervals) <= 1:
            return len(intervals)
        
        cur = intervals[0]
        res = 1
        for interval in intervals[1:]:
            start, end = interval
            if cur[0] <= start and cur[1] >= end:
                continue
            cur = interval
            res += 1
        return res