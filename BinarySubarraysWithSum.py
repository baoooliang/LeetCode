class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        next_1 = {}
        temp = len(A)
        for i in reversed(range(len(A))):
            next_1[i] = temp
            if A[i] == 1:
                temp = i

                left, res, sum_ = 0, 0, 0
        for i in range(len(A)):
            sum_ += A[i]
            while sum_ >= S and left <= i:
                if sum_ == S:
                    res += next_1[i] - i
                sum_ -= A[left]
                left += 1
        
        return res