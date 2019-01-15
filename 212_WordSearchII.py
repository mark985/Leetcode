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
        node = trie.root
        res = []
        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, node, "", res)
        return res

    def dfs(self, board, i, j, node, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == '#':
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = '#'
        self.dfs(board, i - 1, j, node, path + tmp, res)
        self.dfs(board, i + 1, j, node, path + tmp, res)
        self.dfs(board, i, j - 1, node, path + tmp, res)
        self.dfs(board, i, j + 1, node, path + tmp, res)
        board[i][j] = tmp


