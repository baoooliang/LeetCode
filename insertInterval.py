class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        s, e = newInterval
        passed = False
        added = False
        for i in range(len(intervals)):
            start, end = intervals[i]
            if start <= newInterval[1] and end >= newInterval[0]:
                s = min(s, start)
                e = max(e, end)
                passed = True
            else:
                if passed:
                    passed = False
                    added = True
                    res.append([s, e])
                elif newInterval[1] < start and not added:
                    res.append([s, e])
                    added = True
                res.append(intervals[i])
        if not added:
            res.append([s, e])

        return res