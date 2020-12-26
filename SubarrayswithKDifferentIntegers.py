class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def helper(k):
            if k == 0:
                return 0
            res, left, mapper = 0, 0, {}
            for i in range(len(A)):
                if A[i] in mapper:
                    mapper[A[i]] += 1
                else:
                    while left <= i and len(mapper.keys()) >= k:
                        if A[left] in mapper:
                            mapper[A[left]]-=1
                            if mapper[A[left]] == 0:
                                del mapper[A[left]]
                        left+=1
                    mapper[A[i]] = 1
                res += i - left + 1
            return res
        
        return helper(K) - helper(K-1)