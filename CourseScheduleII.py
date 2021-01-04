from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res, degrees, graph = [], [0] * numCourses, [[] for _ in range(numCourses)]
        for c in prerequisites:
            graph[c[1]].append(c[0])
            degrees[c[0]] += 1
        queue = deque(list(filter(lambda i: degrees[i] == 0, range(numCourses))))
        while queue:
            course = queue.popleft()
            res.append(course)
            for child in graph[course]:
                degrees[child] -= 1
                if not degrees[child]:
                    queue.append(child)
            
        return res if sum(degrees) == 0 else []
                