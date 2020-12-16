class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = 0
        sum_ = 0
        res = float('inf')
        for i in range(len(nums)):
            sum_ += nums[i]
            while sum_ >= s:
                res = min(res, i - start + 1)
                sum_ -= nums[start]
                start+=1
        return 0 if res == float('inf') else res