class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(sx,sy,dx,dy):
            queue,seen = collections.deque([(sx,sy,0)]), set([(sx,sy)])
            while queue:
                x,y,count = queue.popleft()
                if x == dx and y == dy:
                    return count
                for _x, _y in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                    if 0 <= _x <len(forest) and 0<=_y<len(forest[0]) and (_x,_y) not in seen and forest[_x][_y] != 0:
                        queue.append((_x,_y,count+1))
                        seen.add((_x,_y))
            return -1
            
        queue = []
        for i in range(len(forest)):
            for j in range(len(forest[i])):
                if forest[i][j] > 1:
                    queue.append((forest[i][j], i, j))
        
        sorted_queue = sorted(queue)
        x, y, res = 0, 0, 0
        for v,dx,dy in sorted_queue:
            steps = bfs(x,y,dx,dy)
            if steps == -1:
                return -1
            res += steps
            x = dx
            y = dy
        
        return res
            