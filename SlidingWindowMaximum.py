from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()  
        
        def reduce(a):
            while queue and queue[-1][1] < nums[a]:
                queue.pop()
            queue.append((a, nums[a]))
                
        for i in range(0, k):
            if not queue:
                queue.append((i, nums[i]))
            else:
                reduce(i)
                
        res = [queue[0][1]]
        i, j = 1, k
        while j < len(nums):
            if queue[0][0] == i-1:
                queue.popleft()
            reduce(j)
            res += [queue[0][1]]
            i+=1
            j+=1
        return res
        