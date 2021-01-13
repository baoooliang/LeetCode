class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        queue = [(grid[0][0], 0, 0)]
        res = 0
        n = len(grid)
        visit = set([0,0])
        while queue:
            value, x, y = heapq.heappop(queue)
            res = max(res, value)
            if x == n-1 and y == n-1:
                return res
            for a, b in [(x-1, y), (x+1,y), (x,y-1), (x,y+1)]:
                if a >= 0 and a < n and b >= 0 and b < n and (a,b) not in visit:
                    visit.add((a,b))
                    heapq.heappush(queue, (grid[a][b], a, b))