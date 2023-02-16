class Solution(object):
    def searchTree(self, parent, order_list):
        if not parent:
            return
        order_list.append(parent.val)
        self.searchTree(parent.left, order_list)
        self.searchTree(parent.right, order_list)
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        order_list = []
        self.searchTree(root, order_list)
        sorted_list = sorted(order_list)
        return sorted_list[k-1]