class Solution(object):
    def pacificAtlantic(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        queue = collections.deque()
        
        def bfs(queue):
            seen = set(queue)
            while queue:
                x,y=queue.popleft()
                for _x, _y in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if 0 <= _x < m and 0 <= _y < n and (_x, _y) not in seen and matrix[x][y] <= matrix[_x][_y]:
                        seen.add((_x,_y))
                        queue.append((_x,_y))
            return seen
        
        queue1 = collections.deque([(i, 0) for i in range(m)] + [(0, j) for j in range(1,n)])
        queue2 = collections.deque([(i, n-1) for i in range(m)] + [(m-1, j) for j in range(0,n-1)])
        result1 = bfs(queue1)
        result2 = bfs(queue2)
        return list(result1 & result2)