 // Dynamic Programming
class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        int len = nums.length;
        int[] dp = new int[len];
        dp[0] = 1;
        int ans = 1;

        for (int i = 1; i < len; i++) {

            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
                else {
                    dp[i] = Math.max(dp[i], 1);
                }
            }

            ans = Math.max(ans, dp[i]);
        }

        return ans;
    }
}

// Binary Search
 public class Solution2 {
     public int lengthOfLIS(int[] nums) {
         int len = nums.length;
         int[] dp = new int[len];
         int ans = 0;

         for (int num : nums) {
             int idx = Arrays.binarySearch(dp, 0, ans, num);
             if (idx < 0) {
                 idx = -(idx + 1);
             }
             dp[idx] = num;
             if (idx == ans) {
                 ans++;
             }
         }

         return ans;
     }
 }
