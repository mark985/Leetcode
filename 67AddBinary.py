class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        maxLen = max(len(a), len(b))
        carry = 0
        result = ''
        for i in range(maxLen):
          charA = '0'
          charB = '0'
          if len(a) > i:
            charA = a[len(a) - i - 1]
          if len(b) > i:
            charB = b[len(b) - i - 1]

          if carry == 1:
            if charA == '1' and charB == '1':
              result = '1' + result
            elif charA == '0' and charB == '0':
              result = '1' + result
              carry = 0
            else:
              result = '0' + result
              carry = 1
          else:
            if charA == '1' and charB == '1':
              result = '0' + result
              carry = 1
            elif charA == '0' and charB == '0':
              result = '0' + result
            else:
              result = '1' + result
        if carry == 1:
          result = '1' + result
        return result