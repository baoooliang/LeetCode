class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]: 
        memo = {}
        road_map = [[] for _ in range(n)]
        for r in roads:
            road_map[r[0]].append(r[1])
            road_map[r[1]].append(r[0])
        
        def dfs(k, depth):
            
            if depth >= len(targetPath):
                return (0, [])
            
            if (k, depth) in memo:
                return memo[(k, depth)]
            
            neighbors = road_map[k] if k != None else list(range(n))
            min_cost = float('inf')
            min_path = None
            for i in neighbors:
                cost = 0
                next_node = dfs(i, depth + 1)
                if names[i] != targetPath[depth]:
                    cost = 1 + next_node[0]
                else:
                    cost = next_node[0]
                if cost < min_cost:
                    min_cost = cost
                    min_path = next_node[1] + [i]
            
            memo[(k, depth)] = (min_cost,min_path)
            return (min_cost,min_path)
        
        return reversed(dfs(None, 0)[1])
        