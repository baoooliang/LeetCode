class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        _set = set()
        def dfs(arr, i, rest):
            if rest == 0:
                res.append(list(arr))
            elif rest < 0:
                return
            
            for j in range(i, len(candidates)):
                rest -= candidates[j]
                dfs(arr + [candidates[j]], j, rest)
                rest += candidates[j]
            
        dfs([], 0, target)
        return res
            
            
            