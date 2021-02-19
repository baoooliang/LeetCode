class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []
        def dfs(i, s):
            if i == len(word):
                res.append(s)
                return
                
            dfs(i+1, s + word[i])
            if i > 0 and not s[-1].isalpha():
                prev = int(s[-1])
                s = s[:len(s)-1] + str(prev+1)
            else:
                s += '1'
            dfs(i+1, s)
        dfs(0, '')
        return res