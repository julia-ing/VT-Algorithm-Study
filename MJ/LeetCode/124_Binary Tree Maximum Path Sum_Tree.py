# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def traverseTree(node):
            if node is None: return -2001

            left = traverseTree(node.left)
            right = traverseTree(node.right)
            path_sum = max(left, right)
            path_sums.append(max(node.val, path_sum+node.val, path_sum, left+right+node.val))
            
            if root != node:
                return max(node.val, path_sum+node.val)
            else:
                return max(node.val, path_sum+node.val,left+right+node.val)

        path_sums = []
        path  = traverseTree(root)
        return max(path_sums)


'''
brute force 접근법을 사용했다.
모든 path의 sum을 저장하지 않고도 최적의 sum을 구할 수 있는 방법이 있을 것 같다. 
개선한다면 리스트를 쓰지 않아도 되어 공간 복잡도를 줄일 수 있을 것이다. 
'''