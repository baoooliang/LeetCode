class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        memo = {}
        def dp(index, amount, height):
            if index == len(rods):
                if amount == 0:
                    return height
                else:
                    return float('-inf')
            
            if (index, amount) in memo:
                return memo[(index, amount)]
            rod = rods[index]
            memo[(index, amount)] = max(dp(index + 1, amount-rods[index], height + rod), dp(index + 1, amount+rods[index], height), dp(index + 1, amount, height))
            return memo[(index, amount)]
            
        return dp(0, 0, 0)