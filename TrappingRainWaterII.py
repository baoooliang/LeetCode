class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        res, queue, seen = 0, [], set()
        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                if i == 0 or j == 0 or i == len(heightMap) - 1 or j == len(heightMap[0]) - 1:
                    heapq.heappush(queue, (heightMap[i][j], i, j))
                    seen.add((i,j))
        
        while queue:
            height, x, y = heapq.heappop(queue)
            for next_x, next_y in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                if next_x < 0 or next_x >= len(heightMap) or next_y < 0 or next_y >= len(heightMap[0]) or (next_x, next_y) in seen:
                    continue
                res += max(0, height - heightMap[next_x][next_y])
                heapq.heappush(queue, (max(heightMap[next_x][next_y], height), next_x, next_y))
                seen.add((next_x, next_y))
        
        return res