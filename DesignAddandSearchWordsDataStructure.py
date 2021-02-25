class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
            
    def search(self, word):
        self.res = False
        self.dfs(self.root, word, 0)
        return self.res
    
    def dfs(self, node, word, index):
        if index == len(word):
            if node.isWord:
                self.res = True
            return
            
        if word[index] == '.':
            for c in node.children:
                self.dfs(node.children[c], word, index + 1)

        else:
            next_node = node.children.get(word[index])
            if not next_node:
                return
            self.dfs(next_node, word, index + 1)
            
        
        
            
        
class WordDictionary:
    def __init__(self):
        self.trie = Trie()
        

    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)
        