# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def traverseTree(node):
            if node is None: return -2001

            left = traverseTree(node.left)
            right = traverseTree(node.right)
            path_sum = max(left, right)
            path_sums.append(max(node.val, path_sum+node.val, path_sum, left+right+node.val))
            
            if root != node:
                return max(node.val, path_sum+node.val)
            else:
                return max(node.val, path_sum+node.val,left+right+node.val)

        path_sums = []
        path  = traverseTree(root)
        return max(path_sums)


