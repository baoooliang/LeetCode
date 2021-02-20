class Solution:
    def isPalindrome(self, start, end, s):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i, part):
            if i >= len(s):
                res.append(list(part))
                return
            for j in range(i, len(s)):
                if self.isPalindrome(i, j, s):
                    part.append(s[i:j+1])
                    dfs(j+1, part)
                    part.pop()
        dfs(0, [])
        return res