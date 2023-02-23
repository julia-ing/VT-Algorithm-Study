class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(r):
            if r:
                return inorder(r.left) + [r.val] + inorder(r.right)
            else:
                return []
        return inorder(root)[k-1]
