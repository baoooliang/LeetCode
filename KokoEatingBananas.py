class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed):
            total = 0
            for p in piles:
                total += int((p-1)/speed) + 1
            return total <= h
        
        left, right = 1, max(piles)
        while left < right:
            mid = int((left + right) / 2)
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left