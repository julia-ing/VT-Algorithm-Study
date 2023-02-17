# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
# O(n)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def tree_to_list(root) -> list:
            if not root: # 노드가 더이상 존재하지 않을 때
                return []

            return tree_to_list(root.left) + [root.val] + tree_to_list(root.right)
        
        tree_list = tree_to_list(root)
        return tree_list[k-1]


# iterative
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
