class Solution:
    def dist(a, b):
        j = 0
        for i in range(0, min(len(a), len(b))):
            if a[i:] == b[:i]:
                j = i
        return len(b) - j
                       
    def shortestSuperstring(self, A: List[str]) -> str:
        g = {}
        for i in range(0, len(A)):
            for j in range(0, len(A)):
                g[(i,j)] = dist(A[i], A[j])
        
        dp = [[float('inf')] * len(A)] * size
        size = 1 << len(A)
        parent = {}
        
        for r in range(0, len(A)):
            dp[(1 << r)][r] = len(A[r])
            
        for s in range(0, size):
            for i in range(0, len(A)):
                if s & (1 << i) == 0:
                    continue
                prev = s - (1 << i)
                for j in range(0, len(A)):
                    if dp[prev][j] + g[(j,i)] < dp[s][i]:
                        dp[s][i] = dp[prev][j] + g[(j,i)]
                        parent[(s,i)] = j
        
        trace_back()