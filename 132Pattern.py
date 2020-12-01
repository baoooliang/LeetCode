class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_arr = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            min_arr[i] = min(nums[i], min_arr[i-1]) if i > 0 else nums[0]
        
        stack = []
        for j in reversed(range(len(nums))):
            if nums[j] > min_arr[j]:
                while stack and stack[-1] <= min_arr[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack += [nums[j]]
        return False