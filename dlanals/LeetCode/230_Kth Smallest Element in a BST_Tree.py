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
        n=0
        stack=[]
        cur=root
        
        while cur or stack : # 노드가 더이상 없고 stack이 empty할 때까지
            while cur : # 노드 전부 순회
                stack.append(cur)
                cur=cur.left # 왼쪽으로 내려가며 stack에 append
            cur=stack.pop()
            n +=1
            
            if n==k : k번째 pop
                return cur.val
            cur = cur.right
