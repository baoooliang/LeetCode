class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        queue = [(0, src, -1)]
        while queue:
            p, node, k = heapq.heappop(queue)
            if k > K:
                continue
            if node == dst:
                return p
            for child, price in graph[node]:
                heapq.heappush(queue, (price + p, child, k+1))
        
        return -1