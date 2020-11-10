class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        memo = {}
        def dp(i, j):
            if i>j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            while i<j and arr[j] == arr[j-1]:
                j-=1
            memo[(i,j)] = 1 + dp(i, j-1)
            for k in range(i, j):
                if arr[k] == arr[j]:
                    left = max(1, dp(k+1, j-1))
                    right = dp(i,k-1)
                    memo[(i,j)] = min(memo[(i,j)], left + right)
            return memo[i,j]   
        
        return dp(0, len(arr)-1)