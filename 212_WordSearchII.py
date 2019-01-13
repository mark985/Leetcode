class TrieNode(object):
    """docstring for TrieNode"""
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie(object):
    """docstring for Trie"""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.isWord = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.isWord
        
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie, "")

        res = set()
        for word in words:
            if trie.search(word):
                res.add(word)
        return list(res)

    def dfs(self, board, i, j, trie, cur):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '#':
            return False
        temp = board[i][j]
        board[i][j] = '#'
        cur += temp
        res = self.dfs(board, i - 1, j, trie, cur) or self.dfs(board, i + 1, j, trie, cur)\
            or self.dfs(board, i, j - 1, trie, cur) or self.dfs(board, i, j + 1, trie, cur)
        board[i][j] = temp
        if res == False:
            trie.insert(cur)
        return False
