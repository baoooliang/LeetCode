class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(word1, word2, i, j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return 1+dfs(word1, word2, i, j+1)
            if j == len(word2):
                return 1+dfs(word1, word2, i+1, j)
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(word1, word2, i+1, j+1)
            else:
                insert = 1+dfs(word1, word2, i, j+1)
                delete = 1+dfs(word1, word2, i+1, j)
                replace = 1+dfs(word1, word2, i+1, j+1)
                memo[(i,j)] = min(insert, delete, replace)
            return memo[(i,j)]
        return dfs(word1, word2,0,0)
                
                