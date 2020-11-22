class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:  
        memo = {}
        def dfs(i, j):           
            if i >= j:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if s[i] == s[j]:
                memo[(i,j)] = dfs(i+1, j-1)
            else:            
                memo[(i,j)] = min(dfs(i+1, j) + 1, dfs(i, j-1) +1)       
            return memo[(i,j)]
        
        return dfs(0, len(s)-1) <= k