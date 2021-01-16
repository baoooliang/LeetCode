class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neibors(n):
            res = []
            for i in range(4):
                num = int(n[i])
                next_digit = num + 1 if num != 9 else 0            
                res.append(f'{n[:i]}{next_digit}{n[i+1:]}')
                prev_digit = num - 1 if num != 0 else 9
                res.append(f'{n[:i]}{prev_digit}{n[i+1:]}')
            return res
        
        if '0000' in deadends or target in deadends:
            return -1
        
        queue,seen = collections.deque([('0000', 0)]), set()
        while queue:
            element, turns = queue.popleft()
            if element == target:
                return turns
            if element in seen:
                continue
            seen.add(element)
            for n in neibors(element):
                if n not in deadends:
                    queue.append((n, turns+1))
        
        return -1
            