class Solution:
    def countArrangement(self, n: int) -> int:
        
        self.res = 0
        nums = list(range(1, n+1))
        
        def dfs(nums, i):
            if not nums:
                self.res += 1
                return
            for j, num in enumerate(nums):
                if num % i == 0 or i % num == 0:
                    dfs(nums[:j] + nums[j+1:], i+1)
                    
        dfs(nums, 1)
        return self.res