class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        queue = [(0,0,0)]
        seen = set()
        dirs = [0, (0,1), (0,-1), (1,0), (-1,0)]
        while queue:
            counts, x, y = heapq.heappop(queue)
            if x == m-1 and y == n-1:
                return counts
            
            if (x,y) in seen:
                continue
            seen.add((x,y))
            
            for i in range(1,5):
                _x, _y = x + dirs[i][0], y + dirs[i][1]
                if 0 <= _x < m and 0 <= _y < n:
                    new_counts = counts if grid[x][y] == i else (counts + 1)
                    heapq.heappush(queue, (new_counts, _x, _y))