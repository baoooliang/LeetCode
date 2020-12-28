from collections import deque

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        pre_sum, queue, res = [0], deque(), float('inf')
        for x in A:
            pre_sum.append(pre_sum[-1] + x)
        
        for i in range(len(A)+1):
            while queue and pre_sum[i] - pre_sum[queue[0]] >= K:
                res = min(res, i - queue[0])
                queue.popleft()
            while queue and pre_sum[i] <= pre_sum[queue[-1]]:
                queue.pop()
            queue.append(i)
        
        return -1 if res == float('inf') else res
        