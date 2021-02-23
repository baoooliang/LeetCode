class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, w):
        node = self.root
        for char in w:
            node = node.children[char]
        node.isWord = True
            
            

class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, trie.root, '', res, board)
        return res
    
    def dfs(self, i, j, node, path, res, board):
        if node.isWord:
            res.append(path)
            node.isWord = False
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        
        temp = board[i][j]
        n = node.children.get(temp)
        if not n:
            return
        
        board[i][j] = '#'
        self.dfs(i+1, j, n, path+temp, res, board)
        self.dfs(i-1, j, n, path+temp, res, board)
        self.dfs(i, j+1, n, path+temp, res, board)
        self.dfs(i, j-1, n, path+temp, res, board)
        board[i][j] = temp
        
        