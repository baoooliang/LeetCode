class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(index, nums):
            if index >= len(nums):
                return 0
            if index in memo:
                return memo[index]
            
            optimal = max(nums[index] + dp(index + 2, nums), dp(index+1, nums))
            memo[index] = optimal
            return optimal
        
        return dp(0, nums)