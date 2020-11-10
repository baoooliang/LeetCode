class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        def dp(i, j):
            if i>j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            while i<j and s[j] == s[j-1]:
                j-=1
            memo[(i,j)] = 1 + dp(i, j-1)
            for k in range(i, j):
                if s[k] == s[j]:
                    memo[(i,j)] = min(memo[(i,j)], dp(k+1, j-1) + dp(i,k))
            return memo[i,j]   
        
        return dp(0, len(s)-1)