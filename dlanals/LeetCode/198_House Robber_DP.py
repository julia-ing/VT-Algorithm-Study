class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            if i==0 :
                dp[0] = nums[0]
            elif i==1 :
                dp[1] = max(dp[0], nums[1])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n-1]
