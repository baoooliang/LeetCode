class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        queue = []
        for i in range(len(points)):
            start, end = points[i]
            heapq.heappush(queue, (start, False, i))
            heapq.heappush(queue, (end, True, i))
        
        _open = set()
        res = 0
        while queue:
            time, isEnd, index = heapq.heappop(queue)
            if not isEnd and index not in _open:
                _open.add(index)
            if isEnd and index in _open:
                res+=1
                _open = set()
        return res
            
        