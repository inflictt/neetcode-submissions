# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # so at each node the diff should be less then equal to 1
    # so at each node calc both height would be counted and then cehckd if the diff of them is <=1 then it would be passed 
        def getHt(root):
            if not root:
                return 0
            l = getHt(root.left)
            r = getHt(root.right)
            return 1 + max(l,r)

        def solve(root):
            if not root:
                return
            leftHT = getHt(root.left)
            rightHT = getHt(root.right)
            check = abs(leftHT-rightHT)
            if check > 1:
                return False
            if solve(root.left) == False:
                return False
            if solve(root.right) == False:
                return False
            return True
        return False if solve(root)==False else True
            
            
