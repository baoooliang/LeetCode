from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses
        for p in prerequisites:
            graph[p[1]] += [p[0]]
            degrees[p[0]] += 1
        queue = deque(list(filter(lambda i: degrees[i] == 0, range(len(degrees)))))
        while queue:
            course = queue.popleft()
            for child in graph[course]:
                degrees[child] -= 1
                if not degrees[child]:
                    queue.append(child)
        return sum(degrees) == 0