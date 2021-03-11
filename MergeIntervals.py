class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        queue = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            heapq.heappush(queue, (start, False, i))
            heapq.heappush(queue, (end, True, i))
            
        _set = set()
        _start, _end = -1, -1
        res = []
        while queue:
            time, isEnd, index = heapq.heappop(queue)
            
            if not isEnd and index not in _set:
                if len(_set) == 0:
                    _start = time
                _set.add(index)
                
            if isEnd and index in _set:
                _set.remove(index)
                if len(_set) == 0:
                    res.append([_start, time])
        
        return res
            