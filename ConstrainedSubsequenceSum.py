from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res, queue = float('-inf'), deque()
        for i in range(len(nums)):
            if queue and i - queue[0][0] > k:
                queue.popleft()
            new_sum = (max(queue[0][1], 0) if queue else 0) + nums[i]
            while queue and queue[-1][1] < new_sum:
                queue.pop()
            queue.append((i, new_sum))
            res = max(res, new_sum)
        return res
            