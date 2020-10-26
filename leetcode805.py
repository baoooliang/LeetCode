class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        memo = {}
        def dp(s,l,index):
            if l == 0:
                return s == 0
            if index == length:
                return False
            if (s, l, index) in memo:
                return memo[(s, l, index)]
            memo[(s, l, index)] = dp(s, l, index + 1) or dp(s-A[index], l-1, index + 1)
            return memo[(s, l, index)] 
        
        length = len(A)
        sumA = sum(A)
        lengthB = length // 2 + 1
        any(dp(sumA * a // length, a, 0) for a in range(1, lengthB) if sumA * a % length == 0)
            