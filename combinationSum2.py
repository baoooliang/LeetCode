class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(arr, target, start, counter):
            if target == 0:
                res.append(list(arr))
                return
            elif target < 0:
                return
            for i in range(start, len(counter)):
                candidate, freq = counter[i]
                if freq <= 0:
                    continue
                arr += [candidate]
                counter[i] = (candidate, freq - 1)
                dfs(arr, target - candidate, i, counter)
                arr.pop()
                counter[i] = (candidate, freq)
                
        counter = Counter(candidates)
        counter = [(key, counter[key]) for key in counter.keys()]
        dfs([], target, 0, counter)
        return res