from heapq import heappush, heappop
class Solution(object):
    def rectangleArea(self, recs):
        _set = set()
        queue = []
        for x1,y1,x2,y2 in recs:
            _set.add(x1)
            _set.add(x2)
            heapq.heappush(queue, (y1, x1, x2, 1))
            heapq.heappush(queue, (y2, x1, x2, -1))
        
        res = 0
        x_list = sorted(list(_set))
        x_index = {}
        for i,e in enumerate(x_list):
            x_index[e] = i
        
        cur = prev = queue[0][0]
        coverage = collections.defaultdict(int)
        while queue:
            cur = queue[0][0]
            
            for i in range(len(x_list)):
                if coverage[i] > 0:
                    res += (x_list[i+1] - x_list[i]) * (cur - prev)
                    
            
            while queue and queue[0][0] == cur:
                y,x1,x2,count = heapq.heappop(queue)
                for i in range(x_index[x1], x_index[x2]):
                    coverage[i] += count
            
            prev = cur
            if queue:
                cur = queue[0][0]
        
        return res % (10**9 + 7)