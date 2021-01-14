class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = collections.deque([start])
        visit = set()
        while queue:
            element = queue.popleft()
            if element in visit:
                continue
            visit.add(element)
            if arr[element] == 0:
                return True
            if 0 <= element + arr[element] < len(arr):
                queue.append(element + arr[element])
            if 0 <= element - arr[element] < len(arr):
                queue.append(element - arr[element])
        
        return False