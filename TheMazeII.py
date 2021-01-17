class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        queue = [(0, start[0], start[1])]
        seen = set()
        while queue:
            path, x, y = heapq.heappop(queue)
            if x == destination[0] and y == destination[1]:
                return path
            if (x,y) in seen:
                continue
            seen.add((x,y))
            for _x, _y in [(-1,0), (1,0), (0,-1), (0,1)]:
                next_x = x + _x
                next_y = y + _y
                _path = 0
                while 0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and maze[next_x][next_y] == 0:
                    next_x += _x
                    next_y += _y
                    _path += 1
                
                if (next_x - _x, next_y - _y) not in seen:
                    heapq.heappush(queue, (path + _path, next_x - _x, next_y - _y))
        
        return -1