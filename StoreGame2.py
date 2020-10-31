class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        memo = {}
        def dp(index, piles, m):
            if(index > len(piles)):
                return 0
            
            if(index, m) in memo:
                return memo[(index, m)]
            
            if 2*m >=len(piles) - index:
                return sum(piles[index: len(piles)])
            
            max_number = 0
            rest_sum = sum(piles[index:])
            for i in range(1, 2*m + 1):
                new_m = max(i, m)
                best = rest_sum - dp(index+i, piles, new_m)
                max_number = max(max_number, best)
                
            memo[(index, m)] = max_number
            return max_number
        
        return dp(0, piles, 1)