class Solution:
    def expand(self, S: str) -> List[str]:
        res = []
        def helper(word, s):
            if not s:
                res.append(word)
                return
            if s[0] == '{':
                j = s.find('}')
                for c in range(1, j):
                    if s[c] != ',':
                        helper(word + s[c], s[j+1:])
            else:
                helper(word+s[0], s[1:])
        return sorted(res)