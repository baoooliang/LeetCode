class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        max_combo = (0,0)
        max_cover = 0
        if len(customers) <= X:
            max_combo = (0, len(customers)-1)
        else:
            left, right = 0, X - 1
            max_combo = (left, right)
            for i in range(left, right+1):
                if grumpy[i] == 1:
                    max_cover += customers[i]
            
            cur=max_cover
            prev = max_cover
            while right <= len(customers) - 1:
                if left == 0:
                    left += 1
                    right += 1
                    continue
                prev_left = customers[left-1] if grumpy[left-1] else 0
                new_right = customers[right] if grumpy[right] else 0
                cur = prev - prev_left + new_right
                prev = cur
                if cur > max_cover:
                    max_cover = cur
                    max_combo = (left, right)
                
                left += 1
                right += 1
        
        res = 0
        left, right = max_combo
        print(f"{left}, {right}")
        for i in range(len(customers)):
            if i in range(left,right+1) or grumpy[i] == 0:
                res += customers[i]
        
        return res
                
            
                
                
                