class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        memo = {}
        def dp(i,j, piles):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == j:
                return piles[i]
            memo[(i,j)] = max(piles[i]-dp(i+1, j, piles), piles[j]-dp(i,j-1,piles))
            return memo[(i,j)]
        return dp(0, len(piles)-1, piles) > 0