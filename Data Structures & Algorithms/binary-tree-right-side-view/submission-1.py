# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        res = []
        def bfs(root):
            if not root:
                return
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
            
        while q:
            for i in range(len(q)):
                node = q.popleft()
                bfs(node)
                rightSide = node
            if rightSide:
                res.append(rightSide.val)

        return res
        