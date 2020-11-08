class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        if sum(nums) % 2 == 1:
            return False
        def dp(index, target):
            if target == 0:
                return True
            if index == len(nums):
                return False
            if (index, target) in memo:
                return memo[(index, target)]
            memo[(index, target)] = dp(index+1, target-nums[index]) or dp(index+1, target)
            return memo[(index, target)]
        return dp(0, sum(nums)/2)