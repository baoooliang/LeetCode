class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        s, e = toBeRemoved
        res = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            if start < e and end > s:
                if s in range(start, end) and start != s:
                    res.append([start, s])
                if e in range(start, end) and end != e:                   
                    res.append([e, end])
            else:
                res.append([start, end])
        return res