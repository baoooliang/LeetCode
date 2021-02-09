class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i, arr):
            if len(arr) == k:
                res.append(list(arr))
            for j in range(i, n+1):
                arr += [j]
                dfs(j+1, arr)
                arr.pop()
        
        dfs(1, [])
        return res