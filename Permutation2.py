class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1
        def dfs():
            if len(perm) == len(nums):
                res.append(list(perm))
                
            for key in count:
                if count[key] > 0:
                    perm.append(key)
                    count[key] -= 1
                    dfs()
                    count[key] += 1
                    perm.pop()
        dfs()
        return res