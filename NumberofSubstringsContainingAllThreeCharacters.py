import collections
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left, res, k = 0, 0, collections.Counter()
        for i in range(len(s)):
            k[s[i]] += 1
            while len(k) == 3:
                print(i)
                res += len(s) - i
                k[s[left]] -= 1
                if not k[s[left]]: 
                    del k[s[left]]
                left+=1
        return res