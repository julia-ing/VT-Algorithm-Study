class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1] * n
        n_max = 1

        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] < dp[j]+1:
                    dp[i]=dp[j]+1

        for i in range(n):
            n_max = max(dp[i], n_max)

        return n_max
