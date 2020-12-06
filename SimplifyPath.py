class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splited_path = path.split('/')
        for p in splited_path:
            if p and p != '.':
                if stack and p == '..':
                    stack.pop()
                elif p != '..':
                    stack.append(p)
        
        if not stack:
            return '/'
        else:
            return '/' + '/'.join(stack)