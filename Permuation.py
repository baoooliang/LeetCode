class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(arr, new_nums):
            if not new_nums:
                res.append(arr)
            for i in range(len(new_nums)):
                dfs(arr + [new_nums[i]],new_nums[:i] + new_nums[i+1:])
        
        dfs([],nums)
        return res