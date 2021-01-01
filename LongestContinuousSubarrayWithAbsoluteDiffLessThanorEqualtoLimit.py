from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res,l,minq, maxq = float('-inf'), 0,deque(), deque()
        for i in range(len(nums)):
            while minq and nums[minq[-1]] > nums[i]:
                minq.pop()
            while maxq and nums[maxq[-1]] < nums[i]:
                maxq.pop()
            minq.append(i)
            maxq.append(i)
            while l < i and nums[maxq[0]] - nums[minq[0]] > limit:
                l+=1
                if l > minq[0]:
                    minq.popleft()
                if l > maxq[0]:
                    maxq.popleft()
            res = max(res, i - l + 1)
        
        return res