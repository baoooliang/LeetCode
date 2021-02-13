class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(start, arr, rest):
            if len(arr) == k:
                if rest == 0:
                    res.append(list(arr))
                else:
                    return
            if start >= 10:
                return
                
            for i in range(start, 10):
                arr.append(i)
                dfs(i+1, arr, rest - i)
                arr.pop()
        
        dfs(1, [], n)
        return res