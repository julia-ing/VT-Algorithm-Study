# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node):
        if not node: 
            return 0
        
        left_sum=self.dfs(node.left)
        if left_sum<0: left_sum=0
        right_sum=self.dfs(node.right)
        if right_sum<0: right_sum=0

        # max value of the path
        self.max_path = max(self.max_path, left_sum + right_sum + node.val)
        
        # add only one of the paths
        return max(left_sum, right_sum) + node.val
    def maxPathSum(self, root):
        self.max_path = float('-inf')
        self.dfs(root)
        return self.max_path