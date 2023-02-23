/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int sum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        calSum(root);
        return sum;
    }
    
    public int calSum(TreeNode root) {
        if (root == null) { return 0; }
        int left = Math.max(0, calSum(root.left));
        int right = Math.max(0, calSum(root.right));
        sum = Math.max(sum, root.val + left + right);
        return root.val + Math.max(left, right);
    }
}

// TC: 0(N), SC: O(N)
