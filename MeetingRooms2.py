class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        queue = []
        taken = None
        for i in range(len(intervals)):
            start, end = intervals[i]
            heapq.heappush(queue, (start, True, i))
            heapq.heappush(queue, (end, False, i))
        
        while queue:
            time, isStart, index = heapq.heappop(queue)
            if isStart:
                if taken != None:
                    return False
                taken = index
            else:
                if taken != None and index == taken:
                    taken = None
        
        return True