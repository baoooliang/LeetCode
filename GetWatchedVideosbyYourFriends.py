class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        freq = collections.defaultdict(int)
        queue = collections.deque([(id, 0)])
        seen = set([id])
        while queue:
            cur, l = queue.popleft()
            if l == level:
                for v in watchedVideos[cur]:
                    freq[v] += 1
            elif l > level:
                break
            for f in friends[cur]:
                if f in seen:
                    continue
                seen.add(f)
                queue.append((f, l+1))

        queue = []
        res = []
        for k in freq.keys():
            if freq[k] > 0:
                heapq.heappush(queue, (freq[k], k))
        
        while queue:
            char = heapq.heappop(queue)[1]
            res += [char]
        
        return res
        