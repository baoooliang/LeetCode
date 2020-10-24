class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """            
        all_possible = set([0])
        for stone in stones:
            temp = all_possible
            all_possible = set()
            for t in temp:
                all_possible.add(stone + t)
                all_possible.add(stone - t)
        
        min_result = float('inf')
        for a in all_possible:
            if a >= 0 and a < min_result:
                min_result = a
        
        return min_result