class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        def dfs(i, arr):
            if i >= len(S):
                res.append(''.join(list(arr)))
                return
            if not S[i].isalpha():
                arr += [S[i]]
                dfs(i+1, arr)
                arr.pop()
            else:
                arr += [S[i]]
                dfs(i+1, arr)
                arr.pop()
                new = S[i].lower() if S[i].isupper() else S[i].upper()
                arr += [new]
                dfs(i+1,arr)
                arr.pop()
        dfs(0, [])
        return res