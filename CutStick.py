class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}
        def dp(left, right):
            if left >= right:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]
            min_value = float('inf')
            has_cut = False
            for o in cuts:
                if o in range(left+1, right):
                    has_cut = True
                    min_value = min(min_value, right-left+dp(left, o)+dp(o, right))
            if has_cut:
                memo[(left, right)] = min_value
                return min_value
            else:
                return 0
        return dp(0, n)
            