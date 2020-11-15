class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        persons = [[]] * 41
        for i in range (0, len(hats)):
            for j in hats[i]:              
                persons[j]  = persons[j]  + [i]
        M = 10**9 + 7
        size = 1 << (len(hats))
        dp = [0] * size
        dp[0] = 1    
        for i in range(1, 41):
            dp_new = dp.copy()
            for j in range(0, size):
                for k in persons[i]:
                    if ((j >> k) & 1) == 1:
                        continue
                    new_state = j + (1 << k)
                    dp_new[new_state] = (dp_new[new_state] + dp[j]) % M  
            dp = dp_new
        return dp[size - 1]