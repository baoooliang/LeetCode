class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = res = 0
        j = len(nums) - 1
        while i < len(nums):
            if nums[i] + nums[i]  > target:
                break
            while i <= j and nums[i] + nums[j] > target:
                j -= 1  
            gap = j - i + 1
            res += 2**(j - i)
            i += 1
        return res % (10**9 + 7)