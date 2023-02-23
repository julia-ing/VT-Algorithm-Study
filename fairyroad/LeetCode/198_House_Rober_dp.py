class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        else:
            for i in range(2, len(nums)):
                if i == 2:
                    nums[i] = nums[i] + nums[0]
                else:
                    nums[i] = nums[i] + max(nums[i-2], nums[i-3])
        return max(nums)
