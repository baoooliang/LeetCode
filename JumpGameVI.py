from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        queue, dp = deque([0]), {0: nums[0]}
        for i in range(1,len(nums)):
            dp[i] = dp[queue[0]] + nums[i]
            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()
            while queue and i - queue[0] >= k:
                queue.popleft()
            queue.append(i)
        
        return dp[len(nums)-1]