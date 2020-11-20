class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}
        def dfs(s1, s2, i, j):
            
            if i == len(s1) and j == len(s2):
                return 0
            
            if (i, j) in memo:
                return memo[(i,j)]
            
            if i == len(s1):
                memo[(i,j)] = dfs(s1, s2, i, j + 1) + ord(s2[j])
            elif j == len(s2):
                memo[(i,j)] = dfs(s1, s2, i + 1, j) + ord(s1[i])

            elif s1[i] == s2[j]:
                memo[(i, j)] = dfs(s1, s2, i + 1, j + 1)
            else:
                memo[(i, j)] = min(dfs(s1, s2, i + 1, j) + ord(s1[i]), dfs(s1, s2, i, j + 1) + ord(s2[j]))
            
            return memo[(i, j)]
        
        return dfs(s1, s2, 0, 0)