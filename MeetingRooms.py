class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        queue = []
        _set = set()
        max_room = 0
        
        for i in range(len(intervals)):
            start, end = intervals[i]
            heapq.heappush(queue, (start, True, i))
            heapq.heappush(queue, (end, False, i))
        
        while queue:
            time, isStart, index = heapq.heappop(queue)
            if isStart:
                _set.add(index)
            else:
                _set.remove(index)
            
            max_room = max(len(_set), max_room)
        
        return max_room