class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]
        for n in nums:
          newPrems = []
          for perm in perms:
            for i in range(len(perm) + 1):
              newPrems.append(perm[:i] + [n] + perm[i:])
          perms = newPrems
        return perms
