class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        
        def feasible(days):
            total = 0
            sub_total = 0
            for bd in bloomDay:
                if bd <= days:
                    sub_total += 1
                    if sub_total == k:
                        total += 1
                        sub_total = 0
                        if total == m:
                            break
                else:
                    sub_total = 0
            return total >= m
                    
        
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = int((left + right) / 2)
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left