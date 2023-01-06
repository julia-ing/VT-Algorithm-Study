class Solution(object):
    def twoSum(self, nums, target):
        len_num = len(nums)
        for i in range(len_num - 1):
            for j in range(i+1, len_num):
                if nums[i] + nums[j] == target:
                    return [i, j]
