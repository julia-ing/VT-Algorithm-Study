class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buff={}
        for i, n in enumerate(nums):
            d=target-n
            if n in buff:
                return [buff[n],i]
            else:
                buff[d]=i