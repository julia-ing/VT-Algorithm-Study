class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        q = [root]

        while q:
            node = q.pop(0)

            temp=TreeNode(left=node.left)
            node.left=node.right
            node.right=temp.left

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        return root