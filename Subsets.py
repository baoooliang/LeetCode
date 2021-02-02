class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(arr, i):
            if i >= len(nums):
                res.append(arr)
                return

            dfs(arr + [nums[i]], i+1)
            dfs(list(arr), i+1)
        
        dfs([], 0)
        return res