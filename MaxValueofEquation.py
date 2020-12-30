from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue, res = deque(), float('-inf')
        for i in range(len(points)):
            while queue and points[i][0] - queue[0][0] > k:
                queue.popleft()
            if queue:
                res = max(res, queue[0][1] + points[i][1] + points[i][0])
            while queue and queue[-1][1] < points[i][1] - points[i][0]:
                queue.pop()
            queue.append((points[i][0], points[i][1] - points[i][0]))
        return res