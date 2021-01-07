from collections import deque

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res, map_ = [], {}
        graph = [[] for _ in range(n)]
        prev = [set() for _ in range(n)]
        degrees = [0] * n
        
        if not prerequisites:
            return [False] * n
        
        for p in prerequisites:
            graph[p[0]].append(p[1])
            degrees[p[1]] += 1
            prev[p[1]].add(p[0])
        
        queue = deque(list(filter(lambda i: degrees[i] == 0, range(n))))
            
        while queue:
            course = queue.popleft()
            for child in graph[course]:
                prev[child] |= prev[course]
                degrees[child] -= 1
                if not degrees[child]:
                    queue.append(child)
        
        for query in queries:
            res.append(query[0] in prev[query[1]])
        
        return res