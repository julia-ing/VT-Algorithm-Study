# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # 1. traverse binary tree 
        # 2. sort and get an index

        def searchTree(root: Optional[TreeNode]):
            if root is None:
                return
            res.append(root.val)
            searchTree(root.left)
            searchTree(root.right)
            

        res = []
        searchTree(root)
        print(res)
        res.sort()
        return res[k-1]

'''
python
- list는 append
- time complexity: O(n)
'''
