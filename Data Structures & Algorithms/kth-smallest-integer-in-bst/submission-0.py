# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder would give me sorted order
        def inorder(root):
            if not root:
                return 
            # call left then self.arr stor then move to right
            inorder(root.left)
            self.arr.append(root.val)
            inorder(root.right)
        self.arr = []
        inorder(root)
        return self.arr[k-1]