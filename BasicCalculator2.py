class Solution:        
    def calculate(self, s: str) -> int:
        stack = []
        current_n = 0
        sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                current_n = current_n * 10 + int(s[i])
            if (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(current_n)
                elif sign == '-':
                    stack.append(-current_n)
                elif sign == '*':
                    e = stack.pop()
                    stack.append(e * current_n)
                elif sign == '/':
                    e = stack.pop()
                    stack.append((int)(e / current_n))
            
                sign = s[i]
                current_n = 0
        
        return sum(stack)