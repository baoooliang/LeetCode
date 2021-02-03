class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        exists = set()
        res = []
        nums = sorted(nums)
        def dfs(i, arr):
            if i >= len(nums):
                ref = tuple(arr)
                if ref not in exists:
                    exists.add(ref)
                    res.append(arr)
                return
            dfs(i+1, arr)
            dfs(i+1, arr + [nums[i]])
        dfs(0, [])
        return res