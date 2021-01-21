class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n, seen  = len(mat), len(mat[0]), set()
        start = 0
        for i in range(m):
            for j in range(n):
                start += mat[i][j] << (i * n + j)
        queue = collections.deque([(start, 0)])
        seen = set([start])
        while queue:
            matrix, count = queue.popleft()
            if not matrix:
                return count
            
            for i in range(m):
                for j in range(n):
                    next_matrix = matrix
                    for _i, _j in [(i+1,j),(i-1,j),(i,j-1),(i,j+1),(i,j)]:
                        if 0 <= _i < m and 0 <= _j < n:
                            next_matrix  ^= 1 << (_i * n + _j)

                    if next_matrix not in seen:
                        seen.add(next_matrix)
                        queue.append((next_matrix, count + 1))
            
        
        return -1