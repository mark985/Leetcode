class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        for index in range(0, len(strs[0])):
            for word in range(1, len(strs)):
                if len(strs[word]) <= index or strs[word][index] != strs[0][index]:
                    return strs[0][0 : index]
        return strs[0]