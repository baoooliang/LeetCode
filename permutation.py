class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(l, path):
            if not l:
                res.append(path)
            for i in range(len(l)):
                dfs(l[:i]+l[i+1:], path+[l[i]])
        
        dfs(nums, [])
        return res