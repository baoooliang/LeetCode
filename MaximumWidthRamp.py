class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        min_prev = float('inf')
        result = 0
        for i in sorted(range(len(A)), key = A.__getitem__):
            result = max(result, i-min_prev)
            min_prev = min(i, min_prev)
        return result