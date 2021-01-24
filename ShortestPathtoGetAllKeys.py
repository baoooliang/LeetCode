class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        queue = collections.deque([])
        seen = set()
        all_keys = ''
        start_i, start_j = -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j].isalpha() and grid[i][j].islower():
                    all_keys+=grid[i][j]
                if grid[i][j] == '@':
                    start_i,start_j = i,j
        queue.append((start_i,start_j,0,6*[0],all_keys))
        while queue:
            x,y,steps,keys,all_keys = queue.popleft()
            value = grid[x][y]
            new_keys = list(keys)
            if value.isalpha() and value.islower():
                if value in all_keys:
                    all_keys = all_keys.replace(value, '') 
                new_keys[ord(value)-ord('a')] = 1
                if not all_keys:
                    return steps
            
            for _x, _y in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                if 0 <= _x < m and 0 <= _y < n and grid[_x][_y] != '#':
                    next_value = grid[_x][_y]
                    if (next_value.isalpha() and next_value.isupper() and new_keys[ord(next_value.lower()) - ord('a')] == 0) or (_x, _y, tuple(new_keys)) in seen:
                        continue
                    queue.append((_x,_y,steps+1,new_keys, all_keys))
                    seen.add((_x,_y,tuple(new_keys)))
        return -1
                        