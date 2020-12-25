class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for ch in set(s):
            if s.count(ch) < k:
                return max(self.longestSubstring(s_, k) for s_ in s.split(ch))
        return len(s)