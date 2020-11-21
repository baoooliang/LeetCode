class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(word1, word2, i, j):
            if i == len(word1) and j == len(word2):
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i == len(word1):
                memo[(i,j)] = 1+dfs(word1, word2, i,j+1)
            elif j == len(word2):
                memo[(i,j)] = 1+dfs(word1, word2, i+1,j)   
            elif word1[i] == word2[j]:
                memo[(i,j)] = dfs(word1, word2, i+1,j+1)
            else:
                memo[(i,j)] = min(1+dfs(word1,word2,i+1,j), 1+dfs(word1,word2,i,j+1))
            
            return memo[(i,j)]
        
        return dfs(word1, word2, 0,0)