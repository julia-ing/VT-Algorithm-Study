from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = self.solution1(root, k)
        result = self.solution2(root, k)
        result = self.solution3(root, k)

        return result

    def solution1(self, root: Optional[TreeNode], k: int) -> int:
        count = defaultdict(int)
        arr = []

        stack = [root]

        while 0 < len(stack):
            node = stack.pop()
            if node.left!=None:
                stack.append(node.left)
            if node.right!=None:
                stack.append(node.right)

            arr.append(node.val)

        arr = sorted(arr)

        return arr[k-1]

    def solution2(self, root: Optional[TreeNode], k: int) -> int:        
        pos = 0
        ans = 0
        
        current = root
        
        while current and pos < k:
            
            if not current.left:
                pos += 1
                ans = current.val
                current = current.right
            
            else:
                pre = current.left
                while pre.right:
                    pre = pre.right
                
                pre.right = current
                left = current.left
                current.left = None
                current = left
        
        return ans

    def solution3(self, root: Optional[TreeNode], k: int) -> int:
        for i, num in enumerate(self.helper(root),1):
            if i == k: 
                return num

    def helper(self, root: Optional[TreeNode]) -> Generator:
        if root:
            yield from self.helper(root.left)
            yield root.val
            yield from self.helper(root.right)
