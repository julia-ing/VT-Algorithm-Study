class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        sorted_nums = sorted(nums)
        a = sorted_nums[0]
        max_len = cur_len = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == a+1:
                cur_len += 1
            else:
                if cur_len > max_len: max_len = cur_len
                cur_len = 1
            a = sorted_nums[i]
            
        if cur_len > max_len: max_len = cur_len
        return max_len