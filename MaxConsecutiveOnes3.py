class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        for i in range(len(A)):
            K -= 1 - A[i]
            
            if K < 0:
                K += 1 - A[left]
                left += 1
        
        return i - left + 1