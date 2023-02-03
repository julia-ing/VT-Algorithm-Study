# DFS - log(n)
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.ans = float('-inf')
        
        def leftRightSum(root):
            if not root:
                return 0
            l = max(leftRightSum(root.left), 0)
            r = max(leftRightSum(root.right), 0)
            self.ans = max(l+r+root.val, self.ans)
            # print(l, r, root.val, self.ans)
            return max(l, r) + root.val
        
        leftRightSum(root)
        return self.ans
