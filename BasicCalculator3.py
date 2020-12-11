class Solution:        
    def calculate(self, s: str) -> int: 
        s = s + '$'
        def helper(stack, i):
            num = 0
            sign = '+'
            res = 0
            while i < len(s):
                ch = s[i]
                if ch.isdigit():
                    num = 10 * num + int(ch)
                    i+=1
                elif ch == ' ':
                    i+=1
                    continue
                elif ch == '(':
                    res,i = helper([], i+1)
                    num = res
                else:
                    if sign == '+':
                        stack.append(num)
                    if sign == '-':
                        stack.append(-num)
                    if sign == '*':
                        e = stack.pop()
                        stack.append(e*num)
                    if sign == '/':
                        e = stack.pop()
                        stack.append(int(e/num))
                    num = 0
                    i+=1
                    if ch == ')':
                        return sum(stack), i
                    sign = ch
                print(stack)
            return sum(stack)
        
        return helper([], 0)
                        
                    
        
                    
                
                
                