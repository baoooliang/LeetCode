class Solution:
    def minJumps(self, arr: List[int]) -> int:
        _map = collections.defaultdict(list)
        for i in range(len(arr)):
            _map[arr[i]].append(i)
                
        queue, seen, seen_group = collections.deque([(0, 0)]), set(), set()
        while queue:
            num, index = queue.popleft()
            if index == len(arr) - 1:
                return num
            for next_index in [index-1, index+1]:
                if 0 <= next_index < len(arr) and next_index not in seen:
                    queue.append((num+1, next_index))
                    seen.add(next_index)
            
            if arr[index] in seen_group:
                continue
            seen_group.add(arr[index])
            
            for next_index in _map[arr[index]]:
                if next_index not in seen:
                    queue.append((num+1, next_index))
                    seen.add(next_index)