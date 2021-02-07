class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        y_set = set()
        diag_1 = set()
        diag_2 = set()
        res = []
        prototype = '.' * n
        
        def dfs(arr, i):
            if i >= n:
                res.append(arr)
            for j in range(n):
                if j in y_set or i+j in diag_1 or j-i in diag_2:
                    continue
                y_set.add(j)
                diag_1.add(i+j)
                diag_2.add(j-i)
                new_arr = prototype[:j] + 'Q' + prototype[j+1:]
                dfs(arr + [new_arr], i+1)
                y_set.remove(j)
                diag_1.remove(i+j)
                diag_2.remove(j-i)
        
        dfs([], 0)
        return res