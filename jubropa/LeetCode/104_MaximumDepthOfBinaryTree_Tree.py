# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        depth = 1
        queue = [(depth, root)]

        while queue:
            depth, node = queue.pop(0)
            left = node.left
            right = node.right

            next_depth = depth + 1

            if left!=None:
                queue.append((next_depth, left))

            if right!=None:
                queue.append((next_depth, right))

        return depth