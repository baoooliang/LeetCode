class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def feasible(thredhold):
            total = 0
            counter = 1
            for n in nums:
                total += n
                if total > thredhold:
                    total = n
                    counter += 1
                    if counter > m:
                        return False
            return True
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = int((left + right) / 2)
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
            