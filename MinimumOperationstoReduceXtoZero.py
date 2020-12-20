class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left, res = 0, float('-inf')
        target = sum(nums) - x
        
        if target < 0:
            return -1
        
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            if sum_ == target:
                res = max(res, i - left + 1)
            while left <= i and sum_ > target:
                sum_ -= nums[left]
                left += 1
            if sum_ == target:
                res = max(res, i - left + 1)
        return len(nums) - res if res != float('-inf') else -1