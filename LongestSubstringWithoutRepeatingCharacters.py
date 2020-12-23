class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res, set_ = 0, 0, set()
        for i in range(len(s)):
            if s[i] not in set_:
                set_.add(s[i])
            else:
                while s[i] != s[left]:
                    set_.remove(s[left])
                    left += 1
                left += 1
            res = max(res, i - left + 1)
        return res