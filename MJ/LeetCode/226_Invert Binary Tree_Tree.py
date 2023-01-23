# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        print(root)
        # class니까 in-place
        if root is None: # Optional
            return root
        
        self.recursive(root)
        return root
    
    def recursive(self, node: Optional[TreeNode]) -> None:
        if node is None: 
            return
        node.left, node.right = node.right, node.left
        self.recursive(node.left)
        self.recursive(node.right)


# -- 구글링 한 것
# python의 Optional이 java의 Optional과 같은 것인지?