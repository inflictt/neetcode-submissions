# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diam(root):
            if not root:
                return 0

            left = diam(root.left)
            right = diam(root.right)

            self.ans = max(self.ans, left + right)

            return max(left, right) + 1

        if not root:
            return

        self.ans = 0
        diam(root)

        return self.ans