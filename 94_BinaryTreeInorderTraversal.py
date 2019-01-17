# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 1. Use Stack
        # res, stack = [],[]
        # while True:
        #   while root:
        #     stack.append(root.left)
        #     root = root.left
        #   if not stack:
        #     return res
        #   top = stack.pop()
        #   res.append(top.val)
        #   root = top.right

        # 2. Recursive
        res = []
        self.helper(root, res)
        return res
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)