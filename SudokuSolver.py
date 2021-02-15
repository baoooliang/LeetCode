class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_set = collections.defaultdict(set)
        column_set = collections.defaultdict(set)
        block_set = collections.defaultdict(set)
        
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] != '.':
                    v = int(board[i][j])
                    row_set[i].add(v)
                    column_set[j].add(v)
                    block_set[(i // 3, j // 3)].add(v)
        
        def isValid(r, c, val):
            block_id = (r // 3, c // 3)
            return val not in row_set[r] and val not in column_set[c] and val not in block_set[block_id]
        
        n = len(board)
        def dfs(r, c):
            if r == n-1 and c == n:
                return True
            elif c == n:
                r += 1
                c = 0
            
            if board[r][c] != '.':
                return dfs(r, c+1)
            
            box_id = (r // 3, c // 3)
            for i in range(1, n+1):
                if not isValid(r, c, i):
                    continue
                
                board[r][c] = str(i)
                row_set[r].add(i)
                column_set[c].add(i)
                block_set[box_id].add(i)
                
                if dfs(r, c+1):
                    return True
                
                row_set[r].remove(i)
                column_set[c].remove(i)
                block_set[box_id].remove(i)
                board[r][c] = '.'
            
            return False
        
        dfs(0, 0)
                
        