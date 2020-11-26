class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visisted = {}
        for g in range(len(graph)):
            if g not in visisted:
                stack = [g]
                visisted[g] = 0
                while len(stack):
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in visisted:
                            visisted[nei] = visisted[node] ^ 1
                            stack += [nei]
                        elif visisted[nei] == visisted[node]:
                            return False
        return True  