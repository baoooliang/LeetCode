class Solution:
    def alienOrder(self, words: List[str]) -> str:
        res = []
        graph = {}
        degrees = {c : 0 for c in ''.join(words)}
        for word1, word2 in zip(words, words[1:]):
            
            #Handle this case: 'abc', 'ab'
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ''
            for combo in list(zip(word1, word2)):
                if combo[0] != combo[1]:
                    if combo[0] not in graph:
                        graph[combo[0]] = []
                    if combo[1] not in graph[combo[0]]:                        
                        graph[combo[0]].append(combo[1])
                        degrees[combo[1]] += 1
                    break #only need to compare the first non-equal word for each pair 
        
        queue = collections.deque([c for c,v in degrees.items() if v == 0])
        
        while queue:
            word = queue.popleft()
            res.append(word)
            if word not in graph:
                continue
            for child in graph[word]:
                degrees[child] -= 1
                if not degrees[child]:
                    queue.append(child)

        if sum(degrees.values()) > 0:
            return ''
        
        return ''.join(res)