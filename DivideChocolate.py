class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        if len(sweetness) == K + 1:
            return min(sweetness)
        
        def feasible(target):
            _sum = 0
            count = 0
            for s in sweetness:
                _sum += s
                if _sum >= target:
                    _sum = 0
                    count += 1
            return count > K
        
            
        left, right = min(sweetness), int(sum(sweetness) / (K + 1)) + 1

        while left < right:    
            mid = int((left + right + 1) / 2)
            if feasible(mid):
                left = mid
            else:
                right = mid - 1
        return left
            
            
        