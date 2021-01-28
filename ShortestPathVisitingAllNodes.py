class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        queue = collections.deque()
        seen = set()
        size = len(graph)
        for i in range(size):
            queue.append((i, [i]))
        
        def get_key(path, node):
            arr = []
            for i in range(size):
                if i in path:
                    arr += [i]
            return (tuple(arr), node)
        
        while queue:
            n, path = queue.popleft()
            if len(set(path)) == size:
                return len(path) - 1
            for nei in graph[n]:
                new_path = path + [nei]
                key = get_key(new_path, nei)
                if key in seen:
                    continue
                seen.add(key)
                queue.append((nei, new_path))
        return 0