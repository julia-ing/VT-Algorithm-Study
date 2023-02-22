class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for i, ele in enumerate(nums):
            if i - 2 >= 0:
                dp_temp = dp[:i-1]
                dp.append(max(dp_temp) + ele)
            else:
                dp.append(nums[i])
        return max(dp)