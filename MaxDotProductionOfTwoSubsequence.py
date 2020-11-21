class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        def dfs(nums1, nums2, i, j):
            if i == len(nums1) or j == len(nums2):
                return float('-inf')
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = max(
                 nums1[i] * nums2[j] + max(dfs(nums1, nums2, i+1, j+1), 0),
                dfs(nums1, nums2, i, j+1),
                dfs(nums1, nums2, i+1, j)
            )
            return memo[(i,j)]
        
        return dfs(nums1, nums2, 0, 0)

