class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def dp(i, j):
            if i == j:
                return nums[i]
            else:
                if (i,j) in memo:
                    return memo[(i,j)]
                memo[(i,j)] = max(nums[i]-dp(i+1,j), nums[j]-dp(i,j-1))
                return memo[(i,j)]
        return dp(0,len(nums)-1) >= 0
        