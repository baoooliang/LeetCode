class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        _map = {}
        seen = set()
        for e in employees:
            _map[e.id] = (e.importance, e.subordinates)
        
        def dfs(eid):
            importance, sub = _map[eid]
            return importance + sum(dfs(s) for s in sub)
        return dfs(id)