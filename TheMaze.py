class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue, seen = collections.deque([(start[0], start[1])]), set()
        if maze[start[0]][start[1]] == 1 or maze[destination[0]][destination[1]] == 1:
            return False
        while queue:
            x, y = queue.popleft()
            if x == destination[0] and y == destination[1]:
                return True
            if (x,y) in seen:
                continue
            seen.add((x,y))
            for _x, _y in [(-1, 0), (1,0), (0,-1), (0,1)]:
                position_x = x + _x
                position_y = y + _y
                while 0 <= position_x < len(maze) and 0 <= position_y < len(maze[0]) and maze[position_x][position_y] == 0:
                    position_x += _x
                    position_y += _y
                    
                queue.append((position_x - _x, position_y - _y))
        
        return False
                    
            