class Solution:

    def evaluate_expr(self, stack):
        res = stack.pop()
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
            
        return res

    def calculate(self, s: str) -> int:
        stack = []
        n, operand = 0, 0
        for ch in reversed(s):
            if ch.isdigit():
                operand = operand + (int(ch) * 10 ** n)
                n += 1
            elif ch != ' ':
                if n:
                    stack.append(operand)
                    operand, n = 0, 0
                if stack and ch == '(':
                    res = self.evaluate_expr(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(ch)
        
        if n:
            stack.append(operand)
        
        return self.evaluate_expr(stack)