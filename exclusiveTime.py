class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = {}
        for l in logs:
            split = l.split(':')
            id_ = split[0]
            action = split[1]
            index = int(split[2])
            if split[1] == 'start':
                if id_ not in res:
                    res[id_] = 0
                stack.append((id_, index, 0))
            else:
                element = stack.pop()
                range_ = index - element[1] - element[2] + 1
                res[id_] = res[id_] + range_
                if stack:
                    stack[-1] = (stack[-1][0], stack[-1][1], stack[-1][2] + range_ + element[2])
        return list(res.values())