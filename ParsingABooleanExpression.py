class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        mapper = {
            '&': all,
            '|': any,
            '!': lambda x : not x[0]
        }
        stack = []
        res = []
        for ch in expression:
            if ch in mapper:
                stack.append(mapper[ch])
            if ch == 't':
                stack.append(True)
            elif ch == 'f':
                stack.append(False)
            elif ch == '(':
                stack.append('(')
            elif ch == ')':
                while stack and stack[-1] != '(':
                    res.append(stack.pop())
                stack.pop()
                sign = stack.pop()
                if res:
                    stack.append(sign(res))
                    res = []
                
        return stack.pop()
            