class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        pq = [(0, K)]
        dist = {}
        for u, v, w in times:
            graph[u].append((w,v))
        while pq:
            d, n = heapq.heappop(pq)
            if n in dist: 
                continue
            dist[n] = d 
            
            for nei_d, nei in graph[n]:
                if nei not in dist:
                    heapq.heappush(pq, (nei_d + d, nei))
        return max(dist.values()) if len(dist) == N else -1