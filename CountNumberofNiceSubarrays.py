class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        next_odd = {}
        odd = None
        for i in reversed(range(len(nums))):
            if nums[i] % 2 == 1:
                next_odd[i] = odd
                odd = i
            
        left, res = 0, 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                k-=1
            while k <= 0:
                next_ = next_odd[i] if next_odd[i] else len(nums)
                res += next_ - i
                if nums[left] % 2 == 1:
                    k += 1
                left += 1
        
        return res