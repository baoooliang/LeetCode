class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = set()
        def dfs(path, t):
            if path and path not in result:
                result.add(path)
            for i in range(len(t)):
                dfs(path + t[i], t[:i] + t[i+1:])
        dfs('', tiles)
        return len(result)