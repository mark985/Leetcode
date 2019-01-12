class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
          for j in range(len(board[0])):
            if self.check(board, i, j, word):
              return True
        return False


    def check(self, board, i, j, word):
      if len(word) == 0:
        return True      
      if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
        return False
      current = board[i][j]
      board[i][j] = '#'
      res = self.check(board, i - 1, j, word[1:]) or self.check(board, i + 1, j, word[1:]) or self.check(board, i, j - 1, word[1:]) or self.check(board, i, j + 1, word[1:])
      board[i][j] = current
      return res