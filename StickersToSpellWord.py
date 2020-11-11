class Solution:
    def getNextNumber(self, i, target, s):
        for c in s:
            for n in range(0, len(target)):
                if ((i >> n) & 1) == 0 and c == target[n]:
                    i |= (1 << n)
                    break
        return i
    
    def minStickers(self, stickers: List[str], target: str) -> int:
        size = 1 << (len(target))
        dp = [float('inf')] * size
        dp [0] = 0
        for i in range(0, size):
            if dp[i] == float('inf'):
                continue
            for s in stickers:
                next = self.getNextNumber(i, target, s)
                dp[next] = min(dp[next], 1 + dp[i])
            
        return dp[size-1] if dp[size-1] != float('inf') else -1