class Solution:
    def getNextStatus(self, i, req_skills, p):
        for ps in p:
            for r in range(0, len(req_skills)):
                if ((i >> r) & 1) == 0 and ps == req_skills[r]:
                    i |= (1 << r)
                    break
                    
        return i
                
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        size = 1 << len(req_skills)
        
        dp = [[-1]] * size
        dp[0] = []
        for i in range(0, size):
            if dp[i] == [-1]:
                continue
            for p in range(0,len(people)):
                j = self.getNextStatus(i, req_skills, people[p])
                if dp[j] == [-1] or len(dp[j]) > len(dp[i]) + 1:
                    dp[j] = (dp[i] + [p])
        
        return dp[size-1]