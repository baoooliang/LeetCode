class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        res = []
        def dfs(i, s):
            if i >= len(digits):
                res.append(s)
                return
            num = digits[i]
            for j in phone[num]:
                s += j
                dfs(i+1,s)
                s=s[:len(s)-1]
        dfs(0, "")
        return res
            