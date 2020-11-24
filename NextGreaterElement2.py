class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [0]
        n = len(nums)
        result = [-1] * n
        for i in range(1, n * 2):
            next_index = i % n
            while(len(stack) > 0 and nums[stack[-1]] < nums[next_index]):
                index = stack.pop()
                result[index] = nums[next_index]
            stack.append(next_index)
        
        return result