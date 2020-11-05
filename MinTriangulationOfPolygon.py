class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        dp = [[0] * len(A) for x in range(len(A))]
        for j in range(2, len(A)):
            for i in range(j-2, -1, -1):
                min_value = float('inf')
                for k in range(i+1, j):
                    min_value = min(min_value, dp[i][k] + dp[k][j] + A[i] * A[j] *A[k])
                dp[i][j] = min_value
        return dp[0][len(A)-1]
        