from collections import defaultdict
from heapq import *

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.dct = defaultdict(int)

class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.now = self.root
        self.sentence = ''
        for i in range(len(sentences)):
            self.add(sentences[i], times[i])

    def add(self, s, count):
        cur = self.root
        for ch in s:
            cur = cur.children[ch]
            cur.dct[s] += count

    def input(self, c):
        if c == '#':
            self.add(self.sentence, 1)
            self.now = self.root
            self.sentence = ''
            return []
        self.sentence += c
        self.now = self.now.children[c]
        records, res = [], []
        for s, count in self.now.dct.items():
            heappush(records, (-count, s))
        for i in range(3):
            if records:
                _, s = heappop(records)
                res.append(s)
        return res