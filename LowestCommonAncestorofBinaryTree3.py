class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def trace(n):
            node = n
            res = []
            while node:
                res += [node]
                node = node.parent
        
            return res
        
        list_p = trace(p)[::-1]
        list_q = trace(q)[::-1]
        
        
        res = None
        for i in range(min(len(list_p), len(list_q))):
            if list_p[i] == list_q[i]:
                res = list_p[i]
            else:
                break
        
        return res