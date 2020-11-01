class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        def dp(index):
            if index >= len(stoneValue):
                return 0
            if index in memo:
                return memo[index]
            best_choice = float('-inf')
            max_option = min(3, len(stoneValue)) + 1
            for i in range(1, max_option):
                result = sum(stoneValue[index: index+i]) - dp(index+i)
                best_choice = max(best_choice, result)
            
            return best_choice
        
        result = dp(0)
        if result > 0:
            return 'Alice'
        elif result == 0:
            return 'Tie'
        else:
            return 'Bob'