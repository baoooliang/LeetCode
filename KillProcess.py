class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        direct_children = {}
        for i in range(len(ppid)):
            if ppid[i] in direct_children:
                direct_children[ppid[i]] += [pid[i]]
            else:
                direct_children[ppid[i]] = [pid[i]]
        result = []
        def get_all_children(parent):
            nonlocal result
            result += [parent]
            if parent not in direct_children:
                return
            for p in direct_children[parent]:
                get_all_children(p)
        
        get_all_children(kill)
        return result