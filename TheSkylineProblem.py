class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        res = []
        def add_sky(pos, height):
            if not res or res[-1][1] != height:
                res.append([pos, height])
        
        _set = set()
        for x1,x2,y in buildings:
            _set.add(x1)
            _set.add(x2)
        all_points = sorted(list(_set))
        live = []
        i = 0
        
        for t in all_points:
            while i < len(buildings) and buildings[i][0] <= t:
                heapq.heappush(live, (-buildings[i][2], buildings[i][1]))
                i+=1
            
            while live and live[0][1] <= t:
                heapq.heappop(live)
            
            add_sky(t, -live[0][0] if live else 0)
            
        return res
                