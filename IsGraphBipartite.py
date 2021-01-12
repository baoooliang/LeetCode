from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visit = {}
        for i in range(len(graph)):
            if i in visit:
                continue
            queue = deque([i])
            visit[i] = True
            while queue:
                node = queue.popleft()
                is_A = visit[node]
                for child in graph[node]:
                    if child not in visit:
                        visit[child] = not is_A
                        queue.append(child)
                    else:
                        if visit[child] == is_A:
                            return False
                    
        return True