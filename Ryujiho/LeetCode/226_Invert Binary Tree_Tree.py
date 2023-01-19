# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root == None: return None

        # add root node at first
        dq = [root]
        while dq:
            node = dq.pop()
            if node:
                node.left, node.right = node.right, node.left
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return root
