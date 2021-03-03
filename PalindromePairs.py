class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.palindromeChildren = []
        self.index = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word, index):
        node = self.root
        word = word[::-1]
        for i in range(len(word)):
            if word[i:] == word[i:][::-1]:
                node.palindromeChildren.append(index)
            node = node.children[word[i]]
        node.index = index

class Solution:        
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        res = []
        for index, word in enumerate(words):
            trie.add(word, index)
        
        for i, word in enumerate(words):
            node = trie.root
            for j,w in enumerate(word):
                if node.index != -1:
                    if word[j:] == word[j:][::-1]:
                        res.append([i, node.index])
                    
                if not node.children.get(w):
                    break
                
                node = node.children[w]
            else:
                if node.index != -1 and node.index != i:
                    res.append([i, node.index])
                
                for n in node.palindromeChildren:
                    res.append([i, n])
                
        return res
                
            
                    