class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def feasible(divisor):
            _sum = 0
            for n in nums:
                _sum += int((n-1) / divisor) + 1
            return _sum <= threshold
        
        left, right = 1, max(nums)
        while left < right:
            mid = int((left + right) / 2)
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left