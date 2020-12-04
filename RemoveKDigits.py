class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:                
            while stack and stack[-1] > n:      
                if k <= 0:
                    break
                    
                stack.pop()
                k-=1
                
            stack += [n]        
        stack = stack[0:len(stack)-k] if k > 0 else stack
        return "".join(stack).lstrip('0') or '0'