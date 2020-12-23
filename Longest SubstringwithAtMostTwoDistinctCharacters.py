class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res, map_, left = 0, {}, 0
        for i in range(len(s)):
            if s[i] not in map_:
                if len(map_.keys()) >= 2:
                    while not any(v == 0 for v in map_.values()):
                        map_[s[left]] -= 1
                        left+=1
                    del map_[s[left - 1]]
                map_[s[i]] = 1
            else:
                map_[s[i]] += 1
            
            res = max(res, i - left + 1)
        
        return res
             