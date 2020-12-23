class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res, left, mapper = 0, 0, {}
        if k == 0 and s:
            return 0
        
        for i in range(len(s)):
            if s[i] in mapper:
                mapper[s[i]] += 1
            else:
                if len(mapper.keys()) == k:
                    while not any(v == 0 for v in mapper.values()):
                        mapper[s[left]] -= 1
                        left += 1
                    del mapper[s[left-1]]
                mapper[s[i]] = 1
            res = max(res, i - left + 1)
            
        return res