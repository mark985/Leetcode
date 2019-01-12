class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = []
        dic = {'(': ')', '[': ']', '{': '}'}
        for i in range(len(s)):
          if s[i] in ['(', '[', '{']:
            result.append(dic[s[i]])
          elif len(result) == 0 or result.pop() != s[i]:
            return False
        return len(result) == 0
