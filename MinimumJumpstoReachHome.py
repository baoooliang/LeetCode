from collections import deque

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        step = 0
        queue = deque([(0, False)])
        forbidden_set = set(forbidden)
        visit = set()
        visit.add((0, False))
        threhold = max(forbidden) + x + a + b
        
        while queue:
            size = len(queue)
            for _ in range(size):
                pos, is_backward = queue.popleft()

                if pos == x:
                    return step
                    
                new_pos = pos + a
                if (new_pos, False) not in visit and new_pos < threhold and new_pos not in forbidden:
                    queue.append((new_pos, False))
                    visit.add((new_pos, False))
                
                new_pos = pos - b
                if new_pos >= 0 and (new_pos, True) not in visit and new_pos not in forbidden and not is_backward:
                    queue.append((new_pos, True))
                    visit.add((new_pos, True))
            
            step += 1
            
        return -1