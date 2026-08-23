# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs que ds ussed
        if not root:
            return []
        que = deque([root])
        ans = []
        while que:
            lvl = []
            for i in range(len(que)):
                curr = que.popleft()
                lvl.append(curr.val)
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            ans.append(lvl)
        return ans
