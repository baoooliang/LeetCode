class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        
        memo={}
        
        def dp(arr, total):
            if arr in memo:
                return memo[arr]
            if arr[-1] >= total:
                return True
            for i in range(len(arr)):
                if not dp(arr[:i] + arr[i+1:], total-arr[i]):
                    memo[arr] = True
                    return True
            memo[arr] = False
            return False
        
        return dp(tuple(range(1,maxChoosableInteger+1)), desiredTotal)