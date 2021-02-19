class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, p):
            if left > right or left < 0 or right < 0:
                return
            if left == right == 0:
                res.append(p)
                return
            dfs(left-1, right, p + '(')
            dfs(left, right - 1, p + ')')
        dfs(n, n, '')
        return res
            