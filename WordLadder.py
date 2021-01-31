class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        size = len(wordList[0])
        dic = collections.defaultdict(list)
        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(size):
                dic[word[:j] + '*' + word[j+1:]] += [word]
                                     
        queue = collections.deque([(beginWord, 1)])
        seen = set([beginWord])
        while queue:
            word, count = queue.popleft()
            if word == endWord:
                return count
            for i in range(len(word)):
                ref = word[:i] + '*' + word[i+1:]
                if ref in dic:
                    for _next in dic[ref]:
                        if _next in seen or _next == word:
                            continue
                        seen.add(_next)
                        queue.append((_next, count + 1))
        
        return 0