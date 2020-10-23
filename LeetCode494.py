class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def df(amount, index):
            if (amount, index) in map:
                return map[(amount, index)]
            if index == len(nums):
                if amount == 0:
                    return 1
                else:
                    return 0
            map[(amount, index)] = df(amount - nums[index], index+1) + df(amount + nums[index], index+1)
            return map[(amount, index)]
        
        map = {}
        return df(S, 0)