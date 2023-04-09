# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        res = 0
        while stack:
            node = stack.pop()
            
            if node:
                val = node.val
                if low < val:
                    stack.append(node.left)
                if val < high:
                    stack.append(node.right)
                if low <= val <= high:
                    res+=val
        
        return res           