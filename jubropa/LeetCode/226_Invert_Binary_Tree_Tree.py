# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recursionInvert(root)
        return root

    def recursionInvert(self, node:Optional[TreeNode]) -> None:
        if node!=None:
            tmp_left = node.left
            node.left = self.recursionInvert(node.right)
            node.right = self.recursionInvert(tmp_left)
        return node


