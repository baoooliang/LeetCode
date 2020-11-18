class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def dfs(i, j, k, s1, s2,s3):
            if k == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                else:
                    return False
            
            if (i, j) in memo:
                return memo[(i,j)]
            
            if i < len(s1) and j < len(s2) and s1[i] == s2[j] and s2[j] == s3[k]:
                memo[(i, j)] =  dfs(i + 1, j, k + 1, s1, s2,s3) or dfs(i, j + 1, k + 1, s1, s2,s3)
                return memo[(i, j)]
            
            elif i < len(s1) and s1[i] == s3[k]:
                memo[(i, j)] = dfs(i + 1, j, k + 1, s1, s2,s3)
                return memo[(i, j)]
            
            elif j < len(s2) and s2[j] == s3[k]:
                memo[(i, j)] = dfs(i, j + 1, k + 1, s1, s2,s3)
                return memo[(i, j)]
            
        return dfs(0, 0, 0, s1, s2,s3)    