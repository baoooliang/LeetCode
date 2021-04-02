class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def feasible(cap):
            days = 1
            total = 0
            for w in weights:
                if w > cap:
                    return False
                total += w
                if total > cap:
                    total = w
                    days += 1
                if days > D:
                    return False
            return True
        
        left, right = min(weights), sum(weights)
        while left < right:
            mid = int((left + right) / 2)
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left