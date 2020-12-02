class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(s, set_):
            result = 0
            if s:
                for i in range(1, len(s)+1):
                    s1 = s[:i]
                    if s1 not in set_:
                        set_.add(s1)
                        result = max(result, 1 + dfs(s[i:], set_))
                        set_.remove(s1)
            return result

        return dfs(s, set())
            