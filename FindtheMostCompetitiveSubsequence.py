from collections import deque

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:        
        bottom_line = len(nums) - k
        queue = deque()
        for i in range(len(nums)):
            while queue and nums[i] < queue[-1] and bottom_line > 0:
                element = queue.pop()
                bottom_line -= 1
            
            queue.append(nums[i])
                
        result = []
        for q in range(len(queue)):
            if q >= k:
                break
            element = queue.popleft()
            result += [element]
        return result